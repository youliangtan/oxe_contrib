# Austin BUDS

The robot is trying to solve a long-horizon kitchen task by picking up pot, placing the pot in a plate, and push them together using a picked-up tool.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Human_Spacemouse](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Human_Spacemouse.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/austin_buds_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/austin_buds_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{zhu2022bottom,
  title={Bottom-Up Skill Discovery From Unsegmented Demonstrations for Long-Horizon Robot Manipulation},
  author={Zhu, Yifeng and Stone, Peter and Zhu, Yuke},
  journal={IEEE Robotics and Automation Letters},
  volume={7},
  number={2},
  pages={4126--4133},
  year={2022},
  publisher={IEEE}
}