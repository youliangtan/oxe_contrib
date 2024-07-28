from verify_oxe import GitRepoReader
import argparse
import os
from typing import Optional
from rlds_reader import read_single_episode


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

    def get_first_episode(self):
        """
        Read and process TFRecord file using TensorFlow.
        """
        image_buffer = read_single_episode(self.save_path)
        # TODO: export to video?
        return image_buffer


def main():
    parser = argparse.ArgumentParser(description="Analyze a Git repository without downloading.")
    parser.add_argument("repo_id", type=str, default="youliantan/bridge_data",
                        help="dataset repo id of the Hugging Face hub.")
    parser.add_argument("--branch", default="main", help="Branch to analyze (default: main)")
    parser.add_argument("--tmp_save_dir", default="tmp/", help="Path to save the downloaded TFRecord shard.")
    args = parser.parse_args()


    # TODO: download single shard in rlds and try run tensorflow loader
    # 1. try load single shard tfrecord file
    # 2. show the first trajectory
    # 3. if image: dump it to a video file and bot show it on PR
    # 4. if generic array: plot the stats 

    hugging_face_url = f"https://huggingface.co/datasets/{args.repo_id}"
    repo_reader = GitRepoReader(repo_url=hugging_face_url, branch=args.branch)
    downloader = SingleShardReader(repo_reader, args.tmp_save_dir)

    downloader.download_metadata()

    # Assuming you know the name or pattern of the tfrecord files
    tfrecord_files = repo_reader.find_files('*.tfrecord*')
    assert tfrecord_files, "No TFRecord files found in the repository."
    file_name = tfrecord_files[0].name  # Get the first tfrecord file
    print(f" trying to download : {file_name}")

    # file_name = "features.json"
    # save_path = os.path.join(save_path, file_name)
    print(f"  =>> Downloading {file_name} to {args.tmp_save_dir}")

    shard_path = downloader.download_shard(file_name)

    assert shard_path, f"Failed to download {file_name}"
    downloader.get_first_episode()


if __name__ == "__main__":
    main()
