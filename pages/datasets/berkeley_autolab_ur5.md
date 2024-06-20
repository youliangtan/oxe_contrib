# Berkeley Autolab UR5

The data consists of 4 robot manipulation tasks: simple pick-and-place of a stuffed animal between containers, sweeping a cloth, stacking cups, and a more difficult pick-and-place of a bottle that requires precise grasp and 6DOF rotation

**Tags**: [Open-X-Embodiment](./pages/tags/Open-X-Embodiment.md), [Robot:UR5](./pages/tags/Robot:UR5.md), [Single_Arm](./pages/tags/Single_Arm.md), [Human_Spacemouse](./pages/tags/Human_Spacemouse.md), [Scene:Table_Top](./pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/berkeley_autolab_ur5/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/berkeley_autolab_ur5/0.1.0",
)
```


## Citation

@misc{BerkeleyUR5Website,
  title = {Berkeley {UR5} Demonstration Dataset},
  author = {Lawrence Yunliang Chen and Simeon Adebola and Ken Goldberg},
  howpublished = {https://sites.google.com/view/berkeley-ur5/home},
}