import tensorflow as tf
from verify_oxe import GitRepoReader
import argparse
import os


class SingleShardReader:
    def __init__(self, repo_reader):
        self.repo_reader = repo_reader

    def download_shard(self, file_name: str, save_path: str) -> str:
        """
        Download a TFRecord shard from the repository.
        """
        self.repo_reader.download_file(file_name, save_path)
        return save_path

    def read_tfrecord(self, file_path: str):
        """
        Read and process TFRecord file using TensorFlow.
        """
        raw_dataset = tf.data.TFRecordDataset(file_path)
        # Placeholder for TFRecord processing logic
        # Normally you would parse the dataset here with the expected schema
        for raw_record in raw_dataset.take(1):
            print("Reading record:", raw_record)
            # Implement actual decoding logic depending on your TFRecord schema


def main():
    parser = argparse.ArgumentParser(description="Analyze a Git repository without downloading.")
    parser.add_argument("repo_id", type=str, default="youliantan/bridge_data",
                        help="dataset repo id of the Hugging Face hub.")
    parser.add_argument("--branch", default="main", help="Branch to analyze (default: main)")
    parser.add_argument("--tmp_save_dir", default="tmp/", help="Path to save the downloaded TFRecord shard.")

    args = parser.parse_args()
    hugging_face_url = f"https://huggingface.co/datasets/{args.repo_id}"
    repo_reader = GitRepoReader(repo_url=hugging_face_url, branch=args.branch)
    downloader = SingleShardReader(repo_reader)

    try:
        # Assuming you know the name or pattern of the tfrecord files
        tfrecord_files = repo_reader.find_files('*.tfrecord*')
        if tfrecord_files:
            file_name = tfrecord_files[0].name  # Get the first tfrecord file
            print(f" trying to download : {file_name}")
            # exit(0)

            # check if the save path exists, else create it
            save_path = args.tmp_save_dir
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            # save_path = os.path.join(save_path, "first_shard.tfrecord")

            # file_name = "features.json"
            save_path = os.path.join(save_path, file_name)
            print(f"  =>> Downloading {file_name} to {save_path}")
            downloader.download_shard(file_name, save_path)
            # downloader.read_tfrecord(save_path)
        else:
            print("No TFRecord files found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
