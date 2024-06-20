# [BC-Z](././pages/datasets/bc_z.md)

The robot attempts picking, wiping, and placing tasks on a diverse set of objects on a tabletop, along with a few challenging tasks like stacking cups on top of each other.

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/bc_z/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/bc_z/0.1.0",
)
```


## Citation

@inproceedings{jang2021bc,
title={{BC}-Z: Zero-Shot Task Generalization with Robotic Imitation Learning},
author={Eric Jang and Alex Irpan and Mohi Khansari and Daniel Kappler and Frederik Ebert and Corey Lynch and Sergey Levine and Chelsea Finn},
booktitle={5th Annual Conference on Robot Learning},
year={2021},
url={https://openreview.net/forum?id=8kbp23tSGYv}}