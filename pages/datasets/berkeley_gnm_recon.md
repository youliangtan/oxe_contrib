# RECON

Mobile robot explores outdoor environments using a scripted policy

**Tags**: [Open-X-Embodiment](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Jackal](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Robot:Jackal.md), [Wheeled_Robot](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Wheeled_Robot.md), [Scripted](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scripted.md), [Scene:Outdoors](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Outdoors.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/berkeley_gnm_recon/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/berkeley_gnm_recon/0.1.0",
)
```


## Citation

@inproceedings{shah2021rapid,
title={{Rapid Exploration for Open-World Navigation with Latent Goal Models}},
author={Dhruv Shah and Benjamin Eysenbach and Nicholas Rhinehart and Sergey Levine},
booktitle={5th Annual Conference on Robot Learning },
year={2021},
url={https://openreview.net/forum?id=d_SWJhyKfVw}
}