import argparse
import os
from git import Repo, GitCommandError
import shutil
import json
from typing import Optional, List
import fnmatch
from dataclasses import dataclass
import requests
import wget


@dataclass
class OXEDatasetConfig:
    version: str
    dataset_name: str
    num_of_shards: int
    num_of_trajs: int
    observation_keys: List[str]


class GitRepoReader:
    def __init__(self, repo_url: str, branch='main', temp_dir='temp_repo'):
        """
        Initialize the Git repository reader.
        """
        self.temp_dir = os.path.join(os.getcwd(), temp_dir)

        # Create a temporary repo object
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        self.repo = Repo.init(self.temp_dir)

        # Add the remote
        try:
            self.origin = self.repo.create_remote('origin', repo_url)
        except GitCommandError:
            self.origin = self.repo.remote('origin')
            self.origin.set_url(repo_url)

        # Get the remote reference and its tree
        self.origin.fetch()
        remote_ref = self.origin.refs[branch]
        self.tree = remote_ref.commit.tree
        self.all_files = list(self.tree.traverse())

        # print repo url
        self.branch = branch
        print(f"Repo URL: {self.origin.url}")

    def find_file(self, file_name: str) -> Optional[object]:
        """
        This function finds a file by name in the repository tree.
        return the object if found, otherwise None
        """
        for item in self.all_files:
            if file_name == item.name:
                return item
        return None

    def find_files(self, pattern: str) -> List[object]:
        """
        This function finds files by pattern in the repository tree.
        return a list of objects if found, otherwise an empty list
        """
        matches = []
        for item in self.all_files:
            if fnmatch.fnmatch(item.name, pattern):
                matches.append(item)
        return matches

    def read_json(self, file_name: str) -> Optional[dict]:
        """Find the json file and read it"""
        blob = self.find_file(file_name)
        if blob:
            return json.loads(blob.data_stream.read().decode('utf-8'))
        return None

    def download_file(self, file_name: str, download_path: str) -> bool:
        """
        Download a file from the repository.
        """
        blob = self.find_file(file_name)
        if blob is None:
            print(f"File '{file_name}' not found in the repository.")
            return False

        try:
            # Ensure the download path's directory exists
            os.makedirs(os.path.dirname(download_path), exist_ok=True)

            # Check if the file is managed by Git LFS
            if self._is_lfs_pointer(blob):
                # LFS file download
                assert "huggingface" in self.origin.url, "Only support huggingface LFS"
                lfs_file_url = f"{self.origin.url}/resolve/{self.branch}/{blob.path}"
                # download the file
                wget.download(lfs_file_url, download_path)
            else:
                # NON-LFS file download
                download_path = os.path.join(download_path, file_name)
                with open(download_path, 'wb') as file:
                    file.write(blob.data_stream.read())
        except Exception as e:
            print(f"Failed to download file '{file_name}': {e}")
            return False
        return True

    def _is_lfs_pointer(self, blob) -> bool:
        """
        Check if the blob is a Git LFS pointer file.
        """
        content = blob.data_stream.read().decode('utf-8')
        return content.startswith('version https://git-lfs.github.com/spec/')

    def __del__(self):
        self.repo.close()
        shutil.rmtree(self.temp_dir)


####################################################################################

def verify_oxe_repo(repo_url, branch='main') -> Optional[OXEDatasetConfig]:
    """
    A simple verification function to check if the RLDS dataset is in the correct format.
    This checks the metadata, and doesn't require the dataset to be downloaded.
    """
    repo_reader = GitRepoReader(repo_url, branch)

    ##############################################################################
    # Check for dataset_info.json
    dataset_info = repo_reader.read_json('dataset_info.json')
    assert dataset_info, "dataset_info.json not found"

    print("\n Found Dataset Info structure:")
    print(f"Dataset Name: {dataset_info['name']}")
    print(f"Dataset Version: {dataset_info['version']}")

    all_shards = []
    for split in dataset_info['splits']:
        shards = split['shardLengths']
        # convert shards list of str to list of int
        shards = [int(shard) for shard in shards]
        all_shards.extend(shards)

    print(f"Dataset number of shards: {len(all_shards)}")

    ##############################################################################
    # Check for features.json
    features_file = repo_reader.read_json('features.json')
    assert features_file, "features.json not found in Dataset"
    print("\n Found Features structure:")

    features = features_file["featuresDict"]["features"]["steps"]["sequence"]["feature"]["featuresDict"]["features"]
    features_keys = set(features.keys())

    print(f"Features: {features_keys}")
    # ensure data is in RLDS format, make sure the following keys are in the features
    for required_key in ['is_first', 'is_last', 'observation',
                         'is_terminal', 'reward', 'discount', 'action']:
        assert required_key in features_keys, f"Missing key: {required_key} in features"

    # oxe observation is stored as feature dict, ensure it is not empty
    obs_keys = set(features["observation"]["featuresDict"]["features"].keys())
    print(f"Observation keys: {obs_keys}")
    assert len(obs_keys) > 0, "Observation keys in features.json should not be empty"

    ##############################################################################
    tfrecord_files = repo_reader.find_files('*.tfrecord*')
    # print("\n Found TFRecord files:", [f.name for f in tfrecord_files])
    print(f"\nNumber of .tfrecord files: {len(tfrecord_files)}")
    assert len(tfrecord_files) == len(all_shards), "Number of tfrecord files does not match with dataset_info"

    ##############################################################################
    # Check if LICENSE file exists
    license_info = repo_reader.find_file('LICENSE')
    assert license_info, "LICENSE file not found"

    return OXEDatasetConfig(
        version=dataset_info['version'],
        dataset_name=dataset_info['name'],
        num_of_shards=len(all_shards),
        num_of_trajs=sum(all_shards),
        observation_keys=list(obs_keys),
    )


def verify_hg_dataset(repo_id: str) -> bool:
    """
    Check if a huggingface dataset is valid/exist.
    # URL: https://datasets-server.huggingface.co/is-valid?=dataset=$repo_id

    :param repo_id: Hugging Face dataset id
    :return: True if the dataset is valid, otherwise False
    """
    query_url = f"https://datasets-server.huggingface.co/is-valid?dataset={repo_id}"
    response = requests.get(query_url)
    if response.status_code != 200:
        print(f"Failed to check dataset: {response.status_code}")
        print(response.text)
        return False
    if response.json().get('error') or response.json().get('valid') is False:
        print(f"Error: {response.json().get('error')}")
        return False
    return True


if __name__ == "__main__":
    """
    Example:
      python verify_oxe.py https://huggingface.co/datasets/youliangtan/rlds_test_viperx_ds
      python verify_oxe.py https://huggingface.co/datasets/youliangtan/bridge_dataset

    """
    parser = argparse.ArgumentParser(description="Analyze a Git repository without downloading.")
    parser.add_argument("repo_url", help="URL of the Git repository")
    parser.add_argument("--branch", default="main", help="Branch to analyze (default: main)")

    args = parser.parse_args()

    # git based analysis
    config = verify_oxe_repo(args.repo_url, args.branch)

    print("\nDataset Configuration:")
    print(config)
    print("Done!")
