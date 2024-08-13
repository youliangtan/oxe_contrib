from abc import ABC, abstractmethod
import os
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any, Set, Callable


class FaceBlurBase(ABC):
    @abstractmethod
    def blur_faces(self, image: np.ndarray) -> np.ndarray:
        raise NotImplementedError

#####################################################################################


class HaarCascadeFaceBlur(FaceBlurBase):
    def __init__(self, face_cascade_path: str = "haarcascade_frontalface_alt.xml"):
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)
        print("HaarCascadeFaceBlur initialized.")

    def blur_faces(self, image: np.ndarray) -> np.ndarray:
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = self.face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10)
        )

        # Blur each face
        for (x, y, w, h) in faces:
            # Extract the region of the face
            face = image[y:y+h, x:x+w]
            # Blur the face
            face = cv2.GaussianBlur(face, (99, 99), 30)
            # Put the blurred face region back into the image
            image[y:y+h, x:x+w] = face
        return image

#####################################################################################


class MediaPipeFaceBlur(FaceBlurBase):
    def __init__(self, model_asset_path: str = 'detector.tflite'):
        """
        This requires mediapipe to be installed.
          for installation: pip install mediapipe

        Follow: https://ai.google.dev/edge/mediapipe/solutions/vision/face_detector
        """
        import mediapipe as mp
        from mediapipe.tasks import python
        from mediapipe.tasks.python import vision
        import wget
        # check if the model_asset_path exists
        if not os.path.exists(model_asset_path):
            # !wget -q -O detector.tflite -q https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite
            model_url = "https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite"
            print(f"Model asset path: {model_asset_path} does not exist. Downloading model from: {model_url}")
            # would try to download the model asset if it does not exist and rename it to model_asset_path
            print(f"Downloading model from: {model_url}")
            model_asset_path = wget.download(model_url, model_asset_path)
            print(f"Model downloaded to: {model_asset_path}")

        base_options = python.BaseOptions(model_asset_path=model_asset_path)
        options = vision.FaceDetectorOptions(base_options=base_options)
        self.detector = vision.FaceDetector.create_from_options(options)

        # Functional method to replace:
        #       image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        self.image_converter_fn = \
            lambda image: mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

        print("MediaPipeFaceBlur initialized.")

    def blur_faces(self, image: np.ndarray) -> np.ndarray:
        image = self.image_converter_fn(image)
        detection_result = self.detector.detect(image)
        image = np.copy(image.numpy_view())

        # Draw bounding_box and gaussian blur the face region
        for detection in detection_result.detections:
            # Draw bounding_box
            bbox = detection.bounding_box

            # Blur the face region
            face_region = image[bbox.origin_y:bbox.origin_y + bbox.height,
                                bbox.origin_x:bbox.origin_x + bbox.width]
            blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
            image[bbox.origin_y:bbox.origin_y + bbox.height,
                  bbox.origin_x:bbox.origin_x + bbox.width] = blurred_face
        return image


#####################################################################################

class BatchFaceBlur:
    def __init__(self, worker_count: int, type: str = "mediapipe"):
        self.detectors = []
        if type == "mediapipe":
            self.detectors = [MediaPipeFaceBlur() for _ in range(worker_count)]
        elif type == "haar":
            self.detectors = [HaarCascadeFaceBlur() for _ in range(worker_count)]
        else:
            raise ValueError(f"Unknown face_blur type: {type}")
        self.workercount = worker_count

    def _blur_face_worker(self, image: np.ndarray, worker_index: int) -> np.ndarray:
        return self.detectors[worker_index].blur_faces(image)

    def batch_blur_faces(self, images: List[np.ndarray]) -> List[np.ndarray]:
        assert len(images) == self.workercount, "Image count should == worker count"
        with ThreadPoolExecutor(max_workers=self.workercount) as executor:
            results = list(executor.map(self._blur_face_worker,
                           images, range(self.workercount)))
        return results


#####################################################################################


def face_blur_step_transform_fn(image_keys: Set[str], face_blur_type: str) -> Callable:
    """
    Get the step transformation function to blur faces in the images. This is the
    high-level helper function to create a step transformation function that blurs
    faces in the images.

    Args:
        image_keys: Set[str]: Set of image keys in the observation.
        face_blur_type: str: The type of face blurring to apply.

    Returns:
        Callable[[Dict[str, Any]], Dict[str, Any]]: The step transformation function.
    """
    from face_blur import MediaPipeFaceBlur, HaarCascadeFaceBlur, BatchFaceBlur

    # Batch face blurring if there are multiple images
    if len(image_keys) > 1:
        worker_count = len(image_keys)
        print("Using batch face blurring with worker count: ", worker_count)
        _blur_method = BatchFaceBlur(worker_count, type=face_blur_type)

        # callback function to blur faces in the images
        def face_blurring_fn(step: Dict[str, Any]) -> Dict[str, Any]:
            """A function to blur faces in the images."""
            original_images = [step["observation"][key] for key in image_keys]
            blurred_images = _blur_method.batch_blur_faces(original_images)
            for key, img in zip(image_keys, blurred_images):
                step["observation"][key] = img
            return step

    # Single image face blurring
    else:
        # Choose the face blurring method
        if face_blur_type == "mediapipe":
            _blur_method = MediaPipeFaceBlur()
        elif face_blur_type == "haar":
            _blur_method = HaarCascadeFaceBlur()
        else:
            raise ValueError(f"Unknown face_blur_type: {face_blur_type}")

        # callback function to blur faces in the images
        def face_blurring_fn(step: Dict[str, Any]) -> Dict[str, Any]:
            """A function to blur faces in the images."""
            for key in image_keys:
                step["observation"][key] = _blur_method.blur_faces(
                    step["observation"][key])
            return step

    return face_blurring_fn

#####################################################################################


if __name__ == "__main__":
    # NOTE: test impl of face blurring implementation
    # read from webcam
    cap = cv2.VideoCapture(0)
    # face_blur = HaarCascadeFaceBlur()
    face_blur = MediaPipeFaceBlur()
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (900, 600))
        frame = face_blur.blur_faces(frame)
        cv2.imshow("webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    exit(0)
