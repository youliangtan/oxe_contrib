# Stanford MaskVIT Data

The robot randomly pushes and picks objects in a bin, which include stuffed toys, plastic cups and toys, etc, and are periodically shuffled.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Sawyer](oed-playground/tree/master/pages/tags/Robot:Sawyer.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Scripted](oed-playground/tree/master/pages/tags/Scripted.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/stanford_mask_vit_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/stanford_mask_vit_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{gupta2022maskvit,
  title={MaskViT: Masked Visual Pre-Training for Video Prediction},
  author={Agrim Gupta and Stephen Tian and Yunzhi Zhang and Jiajun Wu and Roberto Martín-Martín and Li Fei-Fei},
  booktitle={International Conference on Learning Representations},
  year={2022}
}