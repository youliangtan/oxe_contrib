# Open Cross Embodiment Datasets Contributions

Checkout website at: https://youliangtan.github.io/oxe_contrib/

## Steps to contribute

1. Convert the dataset to RLDS format

There are multiple ways to convert the dataset to RLDS format. Some resources are listed below:
 - oxe_envlogger
 - rlds_converter

1. push the dataset to huggingface

The easiest way to contribute is to push the dataset to huggingface. (example below)
```bash
# Usage:  huggingface-cli upload [dataset_repo_id] [local_path] [path_in_repo] --repo-type dataset
huggingface-cli upload youliangtan/bridge_dataset /path/to/bridge_dataset --repo-type dataset
```

*for more info, refer to [huggingface datasets documentation](https://huggingface.co/docs/datasets/v2.20.0/en/share#share-a-dataset-using-the-cli)*

3. Run verification script (example below)

```bash
python scripts/verify_oxe.py https://huggingface.co/datasets/youliangtan/bridge_dataset
```

4. Open a pull request with the dataset information and wait for review


5. Once the pull request is merged, the dataset will be added to the list


## Contributing

Explain how to contribute here.

To Contibute, we encourage contributor to open a pull request with the following information:

 - Dataset Name
 - Dataset Description
 - Dataset URL
 - Dataset License
 - Dataset Citation
 - Contact Information
 - Suggested Tags

## License 

The curated list is under CC0-1.0 License. Please refer to specific dataset for licensing terms. 
