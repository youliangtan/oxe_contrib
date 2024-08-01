import tensorflow_datasets as tfds
import numpy as np
import argparse
import matplotlib.pyplot as plt
import os
import wandb
import datetime

np.set_printoptions(precision=2)


def get_cameras_keys(obs_keys):
    return [key for key in obs_keys if "image" in key]


def read_single_episode(rlds_dir: str, enable_wandb=False):
    """
    This function reads a single episode from the RLDS dataset
    and log the data to wandb if enable
    """
    ds_builder = tfds.builder_from_directory(rlds_dir)
    dataset = ds_builder.as_dataset(split='all')
    dataset_info = ds_builder.info
    obs_keys = dataset_info.features["steps"]["observation"].keys()

    print("\n info: ", dataset_info)

    if enable_wandb:
        wandb.init(
            project="oxe_contrib",
            config={
                "name": dataset_info.name,
                "version": dataset_info.version,
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "size": dataset_info.dataset_size,
                "total_episodes": dataset_info.splits['all'].num_examples,
                "total_shards": dataset_info.splits['all'].num_shards,
                "obs_keys": list(obs_keys),
            }
        )

    ds_length = len(dataset)
    dataset = dataset.take(ds_length)
    it = iter(dataset)

    episode = next(it)
    steps = episode['steps']

    image_keys = get_cameras_keys(obs_keys)
    image_buffer = {k: [] for k in image_keys}

    # TODO: not all key in dataset is named 'state',
    # and action might not be in np.array format
    other_buffer = {"states": [], "actions": []}

    # loop through the steps in the episode
    for j, step in enumerate(steps):
        action = step["action"]
        state = step['observation']['state']
        # print(f" [step {j}] action: ", action)
        # print(f" [step {j}] state: ", state)

        other_buffer["states"].append(state)
        other_buffer["actions"].append(action)

        log_dict = {f"state_{i}": s for i, s in enumerate(state)}
        action_dict = {f"action_{i}": a for i, a in enumerate(action)}
        log_dict.update(action_dict)  # merge the two dicts for logging

        if "language_text" in step:
            # print(f" [step {j}] lang: ", step["language_text"])
            log_dict["language_text"] = step["language_text"]  # log the language text to wandb

        if image_keys:
            for k in image_keys:
                if k not in step['observation']:
                    continue

                img = step['observation'][k]
                img = np.array(img)
                image_buffer[k].append(img)

                log_dict[k] = wandb.Image(img)  # log the image to wandb

        if enable_wandb:
            wandb.log(log_dict)

    del it, dataset
    return image_buffer, other_buffer


def plot_stats(data: list[np.ndarray], title: str, save_dir=None):
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


def generate_video(image_buffer: list[np.array], save_dir: str):
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
    parser.add_argument("--wandb", action="store_true")
    args = parser.parse_args()

    image_buffers, other_buffer = read_single_episode(args.rlds_dir, args.wandb)

    # save the stats
    if args.save_stats:
        generate_video(image_buffers, args.rlds_dir)
        for k, v in other_buffer.items():
            plot_stats(v, k, args.rlds_dir)

    print("Image buffer keys: ", image_buffers.keys())
