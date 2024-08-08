# Open Cross Embodiment Datasets Contributions

[![Website](https://img.shields.io/website-up-down-green-red/https/youliangtan.github.io/oxe_contrib/)](https://youliangtan.github.io/oxe_contrib/)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

Website: https://youliangtan.github.io/oxe_contrib/

Original OXE website: https://github.com/google-deepmind/open_x_embodiment

Installation

```bash
pip install -r requirements.txt
```

## How to Contribute

Steps to contribute your dataset to OXE:

### Step 1: Convert the dataset to RLDS format

There are multiple ways to convert the dataset to RLDS format. Some useful resources are listed below:
 - [rlds_dataset_builder](https://github.com/kpertsch/rlds_dataset_builder)
 - [oxe_envlogger](https://github.com/rail-berkeley/oxe_envlogger)

### Step 2: Push the dataset to huggingface

The easiest way to contribute is to push the dataset to huggingface. (example below)
```bash
# Usage:  huggingface-cli upload [dataset_repo_id] [local_path] [path_in_repo] --repo-type dataset
huggingface-cli upload youliangtan/bridge_dataset /path/to/local/bridge_dataset --repo-type dataset
```

*for more info, refer to [huggingface datasets documentation](https://huggingface.co/docs/datasets/v2.20.0/en/share#share-a-dataset-using-the-cli)*

Example dataset: https://huggingface.co/datasets/youliangtan/bridge_dataset

### Step 3: Run verification script and plot the dataset

**Verfify remote dataset**
```bash
# Example Usage:
python scripts/verify_oxe.py https://huggingface.co/datasets/youliangtan/bridge_dataset
```

*This script will verify if the dataset is in the correct form of RLDS format, with sufficient metadata and correct licensing information.*

**Generate stats for the dataset**
```bash
# Example Usage:
# --stats_dir <LOCAL_DIR> to save a plot and img mp4 of the trajectory
# --enable_wandb to log the stats to wandb
python scripts/generate_stats.py.py --repo_id youliangtan/bridge_dataset --stats_dir stats/
```

*This will download only a single shard, and read the first episode of the data. The plot is saved in `stats/` directory.*

### Step 4: Open a pull request with the dataset information

User should append the metadata to the file with the dataset information.
 - **docs/oxe_dataset_overview.csv**: Metadata of the dataset, for display on the website
 - **docs/data_sources.yaml**: The source of the dataset, for verfiication purposes

*The CI will automatically verify the dataset and upload the stats to wandb for sanity check*

### Step 5. Wait for PR review to merge the dataset to OXE

Once the PR is opened, the dataset will be reviewed by the OXE team. If the dataset is approved, it will be merged to the official OXE dataset list.


Internally the CI will run:
```bash
python scripts/reshard_rlds.py --rlds_dir <ORIGINAL_DATASET> --output_rlds <RESHARD_BLURED_DATASET> --overwrite --face_blur
```
This script will reshard the dataset, and blur the faces of the human actors in the dataset. You can try to run this script locally to verify the dataset.

*CI will get triggered during approval, automatically pull private datasets, conduct resharding & face blurring, and upload to OXE huggingface account.*

## License

The curated list is under CC0-1.0 License. Please refer to specific dataset for licensing terms. 
