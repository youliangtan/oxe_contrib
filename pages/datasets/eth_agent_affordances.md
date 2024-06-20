# ETH Agent Affordances

The robot opens and closes an oven, starting from different initial positions and door angles.

**Tags**: [Open-X-Embodiment](./pages/tags/Open-X-Embodiment.md), [Robot:Franka](./pages/tags/Robot:Franka.md), [Mobile_Manipulator](./pages/tags/Mobile_Manipulator.md), [Expert_Policy](./pages/tags/Expert_Policy.md), [Scene:Kitchen](./pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/eth_agent_affordances/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/eth_agent_affordances/0.1.0",
)
```


## Citation

@inproceedings{schiavi2023learning,
  title={Learning agent-aware affordances for closed-loop interaction with articulated objects},
  author={Schiavi, Giulio and Wulkop, Paula and Rizzi, Giuseppe and Ott, Lionel and Siegwart, Roland and Chung, Jen Jen},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)},
  pages={5916--5922},
  year={2023},
  organization={IEEE}
}