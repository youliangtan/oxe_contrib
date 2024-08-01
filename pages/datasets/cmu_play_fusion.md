# CMU Play Fusion

The robot plays with 3 complex scenes: a grill with many cooking objects like toaster, pan, etc. It has to pick, open, place, close. It  has to set a table, move plates, cups, utensils. And it has to place dishes in the sink, dishwasher, hand cups etc. 

**Tags**: [Open-X-Embodiment](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Single_Arm.md), [Human_VR](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Human_VR.md), [Scene:Table_Top](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Table_Top.md), [Scene:Kitchen](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/cmu_play_fusion/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/cmu_play_fusion/0.1.0",
)
```


## Citation

@inproceedings{chen2023playfusion,
  title={PlayFusion: Skill Acquisition via Diffusion from Language-Annotated Play},
  author={Chen, Lili and Bahl, Shikhar and Pathak, Deepak},
  booktitle={CoRL},
  year={2023}
}