# KAIST Nonprehensile Objects

The robot performs various non-prehensile manipulation tasks in a tabletop environment. It translates and reorients diverse real-world and 3d-printed objects to a target 6dof pose.

**Tags**: [Open-X-Embodiment](./pages/tags/Open-X-Embodiment.md), [Robot:Franka](./pages/tags/Robot:Franka.md), [Single_Arm](./pages/tags/Single_Arm.md), [Expert_Policy](./pages/tags/Expert_Policy.md), [Scene:Table_Top](./pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/kaist_nonprehensile_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/kaist_nonprehensile_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{kimpre,
  title={Pre-and post-contact policy decomposition for non-prehensile manipulation with zero-shot sim-to-real transfer},
  author={Kim, Minchan and Han, Junhyek and Kim, Jaehyung and Kim, Beomjoon},
  booktitle={2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2023},
  organization={IEEE}
}