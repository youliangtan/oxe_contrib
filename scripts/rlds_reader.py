import tensorflow_datasets as tfds
import numpy as np
import argparse
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)


def get_cameras_keys(obs_keys):
    return [key for key in obs_keys if "image" in key]


def read_single_episode(rlds_dir: str):
    ds_builder = tfds.builder_from_directory(rlds_dir)
    dataset = ds_builder.as_dataset(split='all')
    dataset_info = ds_builder.info
    image_keys = get_cameras_keys(dataset_info.features["steps"]["observation"].keys())

    ds_length = len(dataset)
    dataset = dataset.take(ds_length)
    it = iter(dataset)

    episode = next(it)
    steps = episode['steps']
    print("key in a traj: ", episode.keys())

    image_buffer = {k: [] for k in image_keys}

    for j, step in enumerate(steps):
        # print(step['observation'].keys())
        print(f" [step {j}] action: ", step["action"])
        print(f" [step {j}] state: ", step['observation']['state'])

        if "language_text" in step:
            print(f" [step {j}] lang: ", step["language_text"])

        if image_keys:
            for k in image_keys:
                if k not in step['observation']:
                    continue

                img = step['observation'][k]
                img = np.array(img)
                image_buffer[k].append(img)
    del it, dataset
    return image_buffer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--rlds_dir", type=str, default="test_log2")
    args = parser.parse_args()
    image_buffers = read_single_episode(args.rlds_dir)

    print("Image buffer keys: ", image_buffers.keys())
