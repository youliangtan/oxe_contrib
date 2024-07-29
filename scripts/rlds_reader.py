import tensorflow_datasets as tfds
import numpy as np
import argparse
import matplotlib.pyplot as plt
import os

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
    # TODO: not all key in dataset is named 'state', and action might not be in np.array format
    other_buffers = {"states": [], "actions": []}

    for j, step in enumerate(steps):
        # print(step['observation'].keys())
        print(f" [step {j}] action: ", step["action"])
        print(f" [step {j}] state: ", step['observation']['state'])

        other_buffers["states"].append(step['observation']['state'])
        other_buffers["actions"].append(step["action"])

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
    return image_buffer, other_buffers


def plot_stats(data: list[np.ndarray | float], title: str, save_dir=None):
    """
    Plot the stats of the data
    list is a series of datapoints in timestep
    """
    fig, ax = plt.subplots()
    ax.plot(data)
    ax.set_title(title)
    ax.set_xlabel("Timestep")
    ax.set_ylabel("Value")
    # index for the nparry data
    if isinstance(data[0], np.ndarray):
        ax.legend([f"dim {i}" for i in range(data[0].shape[0])])
    if save_dir:
        plt.savefig(os.path.join(save_dir, f"{title}.png"))
    else:
        plt.show()


def generate_video(image_buffer, save_dir="tmp/"):
    """
    Save the images in the buffer to a video mp4 file
    require: pip install sk-video
    """
    from skvideo.io import vwrite
    # write the video
    for k, images in image_buffer.items():
        if not images:
            continue
        video_path = os.path.join(save_dir, f"{k}.mp4")
        vwrite(video_path, images)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--rlds_dir", type=str)
    parser.add_argument("--save_stats", action="store_true")
    args = parser.parse_args()
    image_buffers, other_buffers = read_single_episode(args.rlds_dir)

    # save the stats
    if args.save_stats:
        generate_video(image_buffers, args.rlds_dir)
        for k, v in other_buffers.items():
            plot_stats(v, k, args.rlds_dir)

    print("Image buffer keys: ", image_buffers.keys())
