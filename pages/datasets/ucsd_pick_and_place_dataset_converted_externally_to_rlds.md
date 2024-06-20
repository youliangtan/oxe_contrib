# UCSD Pick Place

The robot performs pick and place tasks in table top and kitchen scenes. The dataset contains a variety of visual variations.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:xArm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:xArm.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Expert_Policy](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Expert_Policy.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md), [Scene:Kitchen](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/ucsd_pick_and_place_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/ucsd_pick_and_place_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@preprint{Feng2023Finetuning,
	title={Finetuning Offline World Models in the Real World},
	author={Yunhai Feng, Nicklas Hansen, Ziyan Xiong, Chandramouli Rajagopalan, Xiaolong Wang},
	year={2023}
}