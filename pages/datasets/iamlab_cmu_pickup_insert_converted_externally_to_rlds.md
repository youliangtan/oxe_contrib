# CMU Franka Pick-Insert Data

The robot tries to pick up different shaped objects placed in front of it. It also tries to insert particular objects into a cylindrical peg.

**Tags**: [Open-X-Embodiment](./pages/tags/Open-X-Embodiment.md), [Robot:Franka](./pages/tags/Robot:Franka.md), [Single_Arm](./pages/tags/Single_Arm.md), [Human_VR](./pages/tags/Human_VR.md), [Scene:Table_Top](./pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/iamlab_cmu_pickup_insert_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/iamlab_cmu_pickup_insert_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{saxena2023multiresolution,
title={Multi-Resolution Sensing for Real-Time Control with Vision-Language Models},
author={Saumya Saxena and Mohit Sharma and Oliver Kroemer},
booktitle={7th Annual Conference on Robot Learning},
year={2023},
url={https://openreview.net/forum?id=WuBv9-IGDUA}
}