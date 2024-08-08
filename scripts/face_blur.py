import numpy as np
import cv2
from abc import ABC, abstractmethod
import os


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
