# [UCSD_Kitchen](././pages/datasets/ucsd_kitchen_dataset_converted_externally_to_rlds.md)

The dataset offers a comprehensive set of real-world robotic interactions, involving natural language instructions and complex manipulations with kitchen objects.

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/ucsd_kitchen_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/ucsd_kitchen_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@ARTICLE{ucsd_kitchens,
  author = {Ge Yan, Kris Wu, and Xiaolong Wang},
  title = {{ucsd kitchens Dataset}},
  year = {2023},
  month = {August}
}
