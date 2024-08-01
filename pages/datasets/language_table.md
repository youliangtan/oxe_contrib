# Language Table

Robot pushed blocks of different geometric shapes on table top.

**Tags**: [Open-X-Embodiment](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:xArm](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Robot:xArm.md), [Single_Arm](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Single_Arm.md), [Human_VR](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Human_VR.md), [Scene:Table_Top](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/language_table/0.0.1")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/language_table/0.0.1",
)
```


## Citation

@article{lynch2023interactive,
  title={Interactive language: Talking to robots in real time},
  author={Lynch, Corey and Wahid, Ayzaan and Tompson, Jonathan and Ding, Tianli and Betker, James and Baruch, Robert and Armstrong, Travis and Florence, Pete},
  journal={IEEE Robotics and Automation Letters},
  year={2023},
  publisher={IEEE}
}