# Roboturk

Sawyer robots flattens laundry, builds towers from bowls and searches objects.

**Tags**: [Open-X-Embodiment](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Sawyer](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Robot:Sawyer.md), [Single_Arm](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Single_Arm.md), [Human_VR](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Human_VR.md), [Scene:Table_Top](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/roboturk/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/roboturk/0.1.0",
)
```


## Citation

@inproceedings{mandlekar2019scaling,
          title={Scaling robot supervision to hundreds of hours with roboturk: Robotic manipulation dataset through human reasoning and dexterity},
          author={Mandlekar, Ajay and Booher, Jonathan and Spero, Max and Tung, Albert and Gupta, Anchit and Zhu, Yuke and Garg, Animesh and Savarese, Silvio and Fei-Fei, Li},
          booktitle={2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
          pages={1048--1055},
          year={2019},
          organization={IEEE}
        }