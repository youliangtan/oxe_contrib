# Stanford Robocook

In the first task, the robot pinches the dough with an asymmetric gripper / two-rod symmetric gripper / two-plane symmetric gripper. In the second task, the robot presses the dough with a circle press / square press / circle punch / square punch. In the third task, the robot rolls the dough with a large roller / small roller.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Scripted](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scripted.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md), [Scene:Kitchen](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/stanford_robocook_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/stanford_robocook_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{shi2023robocook,
  title={RoboCook: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools},
  author={Shi, Haochen and Xu, Huazhe and Clarke, Samuel and Li, Yunzhu and Wu, Jiajun},
  journal={arXiv preprint arXiv:2306.14447},
  year={2023}
}