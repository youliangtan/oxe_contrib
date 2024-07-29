from verify_oxe import GitRepoReader
import argparse
import os
from typing import Optional
from rlds_reader import read_single_episode, plot_stats, generate_video


class SingleShardReader:
    def __init__(self, repo_reader, save_path):
        self.repo_reader = repo_reader
        # create the save path if it does not exist
        os.makedirs(save_path, exist_ok=True)
        self.save_path = save_path

    def download_metadata(self):
        if self.repo_reader.download_file("features.json", self.save_path) and \
                self.repo_reader.download_file("dataset_info.json", self.save_path):
            print("Downloaded metadata files.")
            return True
        return False

    def download_shard(self, file_name: str) -> Optional[str]:
        """
        Download a TFRecord shard from the repository.
        """
        # check if the file exists in the the saved path
        saved_file = os.path.join(self.save_path, file_name)

        if os.path.exists(saved_file):
            print(f"File already exists in {self.save_path}")
            return saved_file

        # Download the file
        success = self.repo_reader.download_file(file_name, self.save_path)
        return saved_file if success else None

    def read_first_episode(self, stats_dir=None):
        """
        Read and process TFRecord file using TensorFlow.
        """
        image_buffer, other_buffers = read_single_episode(self.save_path)
        # TODO: impl save_stats method
        if stats_dir:
            os.makedirs(stats_dir, exist_ok=True)
            generate_video(image_buffer, stats_dir)
            for k, v in other_buffers.items():
                plot_stats(v, k, stats_dir)


def main():
    parser = argparse.ArgumentParser(description="Analyze a Git repository without downloading.")
    parser.add_argument("--repo_id", type=str, default="youliantan/bridge_data",
                        help="dataset repo id of the Hugging Face hub.")
    parser.add_argument("--branch", default="main", help="Branch to analyze (default: main)")
    parser.add_argument("--tmp_save_dir", default="tmp/", help="Path to save the downloaded TFRecord shard.")
    parser.add_argument("--stats_dir", default="stats/", help="Path to save the stats of the episode.")
    args = parser.parse_args()


    # TODO: download single shard in rlds and try run tensorflow loader
    # 1. try load single shard tfrecord file

    hugging_face_url = f"https://huggingface.co/datasets/{args.repo_id}"
    repo_reader = GitRepoReader(repo_url=hugging_face_url, branch=args.branch)
    downloader = SingleShardReader(repo_reader, args.tmp_save_dir)

    downloader.download_metadata()

    # Assuming you know the name or pattern of the tfrecord files
    tfrecord_files = repo_reader.find_files('*.tfrecord*')
    assert tfrecord_files, "No TFRecord files found in the repository."
    file_name = tfrecord_files[0].name  # Get the first tfrecord file
    print(f" trying to download : {file_name}")

    # Download the first trajectory
    print(f"  =>> Downloading {file_name} to {args.tmp_save_dir}")
    shard_path = downloader.download_shard(file_name)
    assert shard_path, f"Failed to download {file_name}"

    # Read the single shard and plot the stats
    # if image: dump it to a video file and show it on 
    # if generic array: plot the stats 
    downloader.read_first_episode(stats_dir=args.stats_dir)
    print(f"Stats saved to {args.stats_dir}")
    print("Done!")

if __name__ == "__main__":
    main()

# python scripts/plot_oxe_stats.py --repo_id youliangtan/bridge_dataset
# python scripts/plot_oxe_stats.py --repo_id youliangtan/rlds_test_viperx_ds
