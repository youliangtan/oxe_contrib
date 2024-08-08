#!/usr/bin/env python3

"""
NOTE Implementation is modified from the original script:
    https://github.com/rail-berkeley/oxe_envlogger/blob/main/reshard_rlds.py



Example usage:

python reshard_rlds.py
    --rlds_dir /path/to/dataset
    --output_rlds /path/to/output_dir
    --overwrite

python scripts/reshard_rlds.py --rlds_dir ~/rail/manipulator_gym/test_pick20/ \
    --output_rlds /space/pick25_reshard --overwrite
"""

import argparse
import copy
import tensorflow_datasets as tfds
import tensorflow as tf
import os
from typing import Tuple, List, Set, Callable, Optional, Dict, Any
from tensorflow_datasets.core import SequentialWriter
import tqdm


def save_rlds_dataset(
    dataset: tf.data.Dataset,
    dataset_info: tfds.core.DatasetInfo,
    max_episodes_per_shard: int = 1000,
    overwrite: bool = False,
    eps_filtering_fn: Optional[Callable[[int, Dict[str, Any]], bool]] = None,
    step_transform_fn: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
):
    """
    Save the dataset to disk in the RLDS format.

    Args:
        dataset: tf.data.Dataset: The dataset to save.
        dataset_info: tfds.core.DatasetInfo: Information about the dataset.
        max_episodes_per_shard: int: Maximum number of episodes per shard.
        overwrite: bool: Whether to overwrite existing files.
        eps_filtering_fn: Optional[Callable[[int, Dict[str, Any]], bool]]: A function that
            takes an episode index and the episode data and returns a boolean indicating
            whether to include the episode in the saved dataset. Return False to skip
        step_transform_fn: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]: A function that
            takes a step data dictionary and returns a transformed step data dictionary.
    """
    writer = SequentialWriter(
        dataset_info, max_episodes_per_shard, overwrite=overwrite
    )
    writer.initialize_splits(["train"], fail_if_exists=False)

    def recursive_dict_to_numpy(d):
        """
        convert each values in the dict to numpy array
        TODO: THIS IS A HACK!!! since the sequence writer uses
        https://github.com/tensorflow/datasets/blob/ab25353173afa5fa01d03759a5e482c82d4fd889/tensorflow_datasets/core/features/tensor_feature.py#L149
        API, which will throw an error if the input is not a numpy array
        """
        for k, v in d.items():
            if isinstance(v, dict):
                recursive_dict_to_numpy(v)
            else:
                d[k] = v.numpy()
        return d

    # Write episodes to disk
    for idx, episode in enumerate(tqdm.tqdm(dataset, desc="Writing episodes")):
        # Manage non-"steps" keys data, e.g. language_embedding, metadata, etc.
        episodic_data_dict = {
            key: episode[key] for key in episode.keys() if key != "steps"
        }

        # Skip this episode if filter returns False
        if eps_filtering_fn and not eps_filtering_fn(idx, episodic_data_dict):
            continue

        episodic_data_dict = recursive_dict_to_numpy(episodic_data_dict)
        steps = []
        for step in episode["steps"]:
            step = recursive_dict_to_numpy(step)
            step = step_transform_fn(step) if step_transform_fn else step
            steps.append(step)

        # write the episode to the dataset
        writer.add_examples(
            {"train": [{"steps": steps, **episodic_data_dict}]}
        )
    writer.close_all()


def print_yellow(x): return print("\033[93m {}\033[00m" .format(x))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rlds_dir", type=str)
    parser.add_argument("--output_rlds",  type=str, required=True)
    parser.add_argument("--overwrite", action='store_true')
    parser.add_argument("--skip_eps_indices", type=int, nargs='+', default=[],
                        help="List of episode indices to skip")
    parser.add_argument("--shard_size", type=int, default=None, help="Max episodes per shard")
    parser.add_argument("--face_blur", action='store_true', help="Apply face blurring")
    parser.add_argument("--face_blur_type", type=str, default="mediapipe")
    args = parser.parse_args()

    # show content in the directory
    print_yellow(f"Content in the directory: {args.rlds_dir}")
    os.system(f"ls -lh {args.rlds_dir}")

    print("here1")
    import time
    time.sleep(1)

    # Recursively find all datasets in the given directories
    ds_builder = tfds.builder_from_directory(args.rlds_dir)
    # exit with success
    exit(0)
    print("here2")
    time.sleep(1)
    dataset = ds_builder.as_dataset(split='all')
    print("here3")
    time.sleep(1)

    dataset_info = ds_builder.info
    total_size = dataset_info.dataset_size
    recommended_shard_size = round(200*1024*1024*len(dataset)/total_size)

    print_yellow(f"Total size of datasets: {total_size/1024.0} kb")
    print_yellow(f"!!NOTE!! It is recommended to keep tfrecord size at "
                 f"around 200MB. Thus the recommended shard size should "
                 f"be around {recommended_shard_size} episodes. ")

    if args.shard_size is None:
        print_yellow(f"Using the recommended shard size: {recommended_shard_size}")
        shard_size = recommended_shard_size
    else:
        shard_size = args.shard_size

    def update_data_dir(target_dir, dataset_info):
        # Bug in update_data_dir() method, need to update the identity object as well
        # https://github.com/tensorflow/datasets/pull/5297
        # dataset_info.update_data_dir(target_dir) # not supported in MultiSplitInfo()
        dataset_info._identity.data_dir = target_dir

    # Create a new dataset info with the updated data_dir
    dataset_info = copy.deepcopy(dataset_info)
    update_data_dir(args.output_rlds, dataset_info)
    assert dataset_info.data_dir == args.output_rlds
    # print(dataset_info)

    os.makedirs(args.output_rlds, exist_ok=True)

    # For user to skip some episodes
    if args.skip_eps_indices:
        print_yellow(f"Skipping episodes: {args.skip_eps_indices}")
        skip_eps_indices = set(args.skip_eps_indices)

        def eps_filtering_fn(idx, metadata):
            # return false to skip the episode
            return idx not in skip_eps_indices
    else:
        eps_filtering_fn = None

    if args.face_blur:
        from face_blur import MediaPipeFaceBlur, HaarCascadeFaceBlur

        # Choose the face blurring method
        if args.face_blur_type == "mediapipe":
            face_blurring_class = MediaPipeFaceBlur()
        elif args.face_blur_type == "haar":
            face_blurring_class = HaarCascadeFaceBlur()
        else:
            raise ValueError(f"Unknown face_blur_type: {args.face_blur_type}")

        # callback function to blur faces in the images
        def face_blurring_fn(step: Dict[str, Any]) -> Dict[str, Any]:
            """
            A function to blur faces in the images.
            """
            image_keys = set([key for key in step.keys() if "image" in key])
            for key in image_keys:
                step[key] = face_blurring_class.blur_faces(step[key])
            return step
    else:
        face_blurring_fn = None

    # save the merged dataset to disk
    print_yellow(f"Writing episodes to disk: [{args.output_rlds}]")
    save_rlds_dataset(
        dataset=dataset,
        dataset_info=dataset_info,
        max_episodes_per_shard=shard_size,
        overwrite=args.overwrite,
        eps_filtering_fn=eps_filtering_fn,
    )
    print("Updated dataset info: ", dataset_info)
    print_yellow(f"Saved rlds dataset to: {args.output_rlds}")
