# CoryHall

Small mobile robot navigates hallways in an office building using a learned policy.

**Tags**: [Open-X-Embodiment](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:RC_Car](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Robot:RC_Car.md), [Wheeled_Robot](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Wheeled_Robot.md), [Expert_Policy](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Expert_Policy.md), [Scene:Hallways](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Hallways.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/berkeley_gnm_cory_hall/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/berkeley_gnm_cory_hall/0.1.0",
)
```


## Citation

@inproceedings{kahn2018self,
  title={Self-supervised deep reinforcement learning with generalized computation graphs for robot navigation},
  author={Kahn, Gregory and Villaflor, Adam and Ding, Bosen and Abbeel, Pieter and Levine, Sergey},
  booktitle={2018 IEEE international conference on robotics and automation (ICRA)},
  pages={5129--5136},
  year={2018},
  organization={IEEE}
}