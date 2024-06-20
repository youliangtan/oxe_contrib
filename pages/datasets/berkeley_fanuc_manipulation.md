# Berkeley Fanuc Manipulation

A Fanuc robot performs various manipulation tasks. For example, it opens drawers, picks up objects, closes doors, closes computers, and pushes objects to desired locations.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Fanuc_Mate](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Fanuc_Mate.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Human_VR](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Human_VR.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/berkeley_fanuc_manipulation/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/berkeley_fanuc_manipulation/0.1.0",
)
```


## Citation

@article{fanuc_manipulation2023,
  title={Fanuc Manipulation: A Dataset for Learning-based Manipulation with FANUC Mate 200iD Robot},
  author={Zhu, Xinghao and Tian, Ran and Xu, Chenfeng and Ding, Mingyu and Zhan, Wei and Tomizuka, Masayoshi},
  year={2023},
}