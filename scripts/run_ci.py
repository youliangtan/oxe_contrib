import os
import yaml
from verify_oxe import verify_oxe_repo
from generate_stats import generate_stats_from_shard


# Get the last dataset
def read_latest_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['dataset'][-1]


if __name__ == "__main__":
    yaml_file_path = "docs/data_sources.yaml"
    latest_dataset = read_latest_from_yaml(yaml_file_path)
    print(f"Latest dataset: {latest_dataset}")

    # verify the repo
    if latest_dataset['source_type'] == 'huggingface':
        url = f"https://huggingface.co/datasets/{latest_dataset['repo_id']}"
        verify_oxe_repo(url, latest_dataset['branch'])
    else:
        raise ValueError(f"Unknown source type: {latest_dataset['source_type']}")

    generate_stats_from_shard(latest_dataset['repo_id'], latest_dataset['branch'], enable_wandb=True)
    print("Done verifying oxe dataset: ", latest_dataset['repo_id'])
