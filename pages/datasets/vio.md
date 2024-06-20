# Austin VIOLA

The robot performs various household-like tasks, such as setting up the table, or making coffee using a coffee machine. 

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Franka](oed-playground/tree/master/pages/tags/Robot:Franka.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Human_Spacemouse](oed-playground/tree/master/pages/tags/Human_Spacemouse.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/viola/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/viola/0.1.0",
)
```


## Citation

@article{zhu2022viola,
  title={VIOLA: Imitation Learning for Vision-Based Manipulation with Object Proposal Priors},
  author={Zhu, Yifeng and Joshi, Abhishek and Stone, Peter and Zhu, Yuke},
  journal={6th Annual Conference on Robot Learning (CoRL)},
  year={2022}
}