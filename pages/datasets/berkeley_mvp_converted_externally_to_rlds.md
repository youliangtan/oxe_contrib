# [Berkeley_MVP_Data](././pages/datasets/berkeley_mvp_converted_externally_to_rlds.md)

Basic motor control tasks (reach, push, pick) on table top and toy environments (toy kitchen, toy fridge).

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/berkeley_mvp_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/berkeley_mvp_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@InProceedings{Radosavovic2022,
  title = {Real-World Robot Learning with Masked Visual Pre-training},
  author = {Ilija Radosavovic and Tete Xiao and Stephen James and Pieter Abbeel and Jitendra Malik and Trevor Darrell},
  booktitle = {CoRL},
  year = {2022}
}