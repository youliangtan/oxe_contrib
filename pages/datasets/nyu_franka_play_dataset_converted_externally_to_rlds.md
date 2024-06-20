# NYU Franka Play

The robot interacts with a toy kitchen doing arbitrary tasks. It opens/closes the microwave door, opens/closes the oven door, turns the stove knobs, and moves the pot between the stove and the sink.

**Tags**: [Open-X-Embodiment](./pages/tags/Open-X-Embodiment.md), [Robot:Franka](./pages/tags/Robot:Franka.md), [Single_Arm](./pages/tags/Single_Arm.md), [Human_VR](./pages/tags/Human_VR.md), [Scene:Kitchen](./pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/nyu_franka_play_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/nyu_franka_play_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{cui2022play,
  title   = {From Play to Policy: Conditional Behavior Generation from Uncurated Robot Data},
  author  = {Cui, Zichen Jeff and Wang, Yibin and Shafiullah, Nur Muhammad Mahi and Pinto, Lerrel},
  journal = {arXiv preprint arXiv:2210.10047},
  year    = {2022}
}