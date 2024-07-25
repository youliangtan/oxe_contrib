import argparse
import os
from git import Repo, GitCommandError
import shutil
import json
from typing import Optional, List
import fnmatch
from dataclasses import dataclass

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
            origin = self.repo.create_remote('origin', repo_url)
        except GitCommandError:
            origin = self.repo.remote('origin')
            origin.set_url(repo_url)

        # Get the remote reference and its tree
        origin.fetch()
        remote_ref = origin.refs[branch]
        self.tree = remote_ref.commit.tree
        self.all_files = list(self.tree.traverse())

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

    def __del__(self):
        self.repo.close()
        shutil.rmtree(self.temp_dir)


def verify_oxe_repo(repo_url, branch='main') -> Optional[OXEDatasetConfig]:

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
    assert features_file, "features.json not found"
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
    assert len(obs_keys) > 0, "Observation keys should not be empty"

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


def single_shard_tfrecord_loader(repo_url, branch='main'):
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description="Analyze a Git repository without downloading.")
    parser.add_argument("repo_url", help="URL of the Git repository")
    parser.add_argument("--branch", default="main", help="Branch to analyze (default: main)")

    args = parser.parse_args()
    
    # git based analysis
    config = verify_oxe_repo(args.repo_url, args.branch)
    
    # TODO: download single shard in rlds and try run tensorflow loader
    # 1. try load single shard tfrecord file
    # 2. show the first trajectory
    # 3. visualize the camera observation in the first trajectory
    # 4. dump it to a video file and bot show it on PR

    print("\nDataset Configuration:")
    print(config)

if __name__ == "__main__":
    main()

# Example: 
#   python verify_oxe.py https://huggingface.co/datasets/youliangtan/rlds_test_viperx_ds
#   python verify_oxe.py https://huggingface.co/datasets/youliangtan/bridge_dataset
