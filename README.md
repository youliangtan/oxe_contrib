# Open Cross Embodiment Datasets Contributions

Website at: https://youliangtan.github.io/oxe_contrib/

Original OXE website: https://github.com/google-deepmind/open_x_embodiment

## How to Contribute

Steps to contribute your dataset to OXE:

### 1. Convert the dataset to RLDS format

There are multiple ways to convert the dataset to RLDS format. Some useful resources are listed below:
 - [rlds_dataset_builder](https://github.com/kpertsch/rlds_dataset_builder)
 - [oxe_envlogger](https://github.com/rail-berkeley/oxe_envlogger)

### 2. push the dataset to huggingface

The easiest way to contribute is to push the dataset to huggingface. (example below)
```bash
# Usage:  huggingface-cli upload [dataset_repo_id] [local_path] [path_in_repo] --repo-type dataset
huggingface-cli upload youliangtan/bridge_dataset /path/to/local/bridge_dataset --repo-type dataset
```

*for more info, refer to [huggingface datasets documentation](https://huggingface.co/docs/datasets/v2.20.0/en/share#share-a-dataset-using-the-cli)*

Example dataset: https://huggingface.co/datasets/youliangtan/bridge_dataset

### 3. Run verification script and plot the dataset

```bash
python scripts/verify_oxe.py https://huggingface.co/datasets/youliangtan/bridge_dataset
```

This script will verify if the dataset is in the correct form of RLDS format, with sufficient metadata and correct licensing information.


To Generate the dataset stats, run the following script:

```bash
# --stats_dir <LOCAL_DIR> to save a plot and img mp4 of the trajectory, default is stats/
# --enable_wandb to log the stats to wandb
python scripts/generate_oxe_stats.py.py --repo_id youliangtan/bridge_dataset --enable_wandb
```

This will download only a single shard, and read a single episode of the data. The plot is saved in `stats/` directory.

### 4. Open a pull request with the dataset information and wait for review

User should also add the metadata of the dataset in the `csv` file, located in `docs/xxx.csv`

TODO: will trigger CI to run verification script

### 5. Once the pull request is merged, the dataset will be added to the list

TODO: CI will automatically pull private datasets, conduct face blurring, and upload to OXE huggingface account.

## License

The curated list is under CC0-1.0 License. Please refer to specific dataset for licensing terms. 
