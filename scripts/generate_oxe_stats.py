from verify_oxe import GitRepoReader, verify_hg_dataset
import argparse
import os
from rlds_reader import read_single_episode, plot_stats, generate_video


def main():
    parser = argparse.ArgumentParser(description="Analyze a Git repository without downloading.")
    parser.add_argument("--repo_id", type=str, default="youliantan/bridge_data",
                        help="dataset repo id of the Hugging Face hub.")
    parser.add_argument("--branch", default="main", help="Branch to analyze (default: main)")
    parser.add_argument("--tmp_save_dir", default="tmp/", help="Path to save the downloaded TFRecord shard.")
    parser.add_argument("--stats_dir", default=None, help="Path to save the stats of the episode.")
    parser.add_argument("--enable_wandb", action="store_true", help="Enable logging to wandb.")
    args = parser.parse_args()

    # Define the dataset and reader
    assert verify_hg_dataset(args.repo_id), "Dataset is not valid."

    hugging_face_url = f"https://huggingface.co/datasets/{args.repo_id}"
    repo_reader = GitRepoReader(repo_url=hugging_face_url, branch=args.branch)

    # Download metadata files
    assert repo_reader.download_file("features.json", args.tmp_save_dir), "Failed to download features.json"
    assert repo_reader.download_file("dataset_info.json", args.tmp_save_dir), "Failed to download dataset_info.json"

    # Get the first RLDS shard name
    tfrecord_files = repo_reader.find_files('*.tfrecord*')
    assert tfrecord_files, "No TFRecord files found in the repository."
    file_name = tfrecord_files[0].name  # Get the first tfrecord file
    full_shard_path = os.path.join(args.tmp_save_dir, file_name)
    print(f" trying to download : {file_name}")

    # Download the first shard
    print(f"  =>> Downloading {file_name} to {args.tmp_save_dir}")
    if os.path.exists(full_shard_path):
        print(f"File already exists in {args.tmp_save_dir}, will skip downloading.")
    else:
        assert repo_reader.download_file(file_name, args.tmp_save_dir), f"Failed to download {file_name}"

    # Try load single shard tfrecord file
    im_buffer, other_buffer = read_single_episode(args.tmp_save_dir, args.enable_wandb)
    assert im_buffer, "Image buffer is empty, check if the episode has images"
    assert other_buffer, "Other buffer is empty, check if other keys are present in the step of each episode"

    # Read the single shard and plot the stats
    if args.stats_dir:
        os.makedirs(args.stats_dir, exist_ok=True)
        generate_video(im_buffer, args.stats_dir)
        for k, v in other_buffer.items():
            plot_stats(v, k, args.stats_dir)
        print(f"Stats saved to {args.stats_dir}")

    print("Done!")


if __name__ == "__main__":
    main()

# python scripts/plot_oxe_stats.py --repo_id youliangtan/bridge_dataset --enable_wandb
# python scripts/plot_oxe_stats.py --repo_id youliangtan/rlds_test_viperx_ds --enable_wandb
