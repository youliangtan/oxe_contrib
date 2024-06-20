# NYU ROT

The robot arm performs diverse manipulation tasks on a tabletop such an box opening, cup stacking, and pouring, among others. 

**Tags**: [Open-X-Embodiment](./pages/tags/Open-X-Embodiment.md), [Robot:xArm](./pages/tags/Robot:xArm.md), [Single_Arm](./pages/tags/Single_Arm.md), [Human_Joystick](./pages/tags/Human_Joystick.md), [Scene:Table_Top](./pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/nyu_rot_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/nyu_rot_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{haldar2023watch,
  title={Watch and match: Supercharging imitation with regularized optimal transport},
  author={Haldar, Siddhant and Mathur, Vaibhav and Yarats, Denis and Pinto, Lerrel},
  booktitle={Conference on Robot Learning},
  pages={32--43},
  year={2023},
  organization={PMLR}
}