# QT-Opt

Kuka robot picking objects in a bin.

**Tags**: [Open-X-Embodiment](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Kuka_iiwa](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Robot:Kuka_iiwa.md), [Single_Arm](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Single_Arm.md), [Expert_Policy](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Expert_Policy.md), [Scene:Table_Top](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/kuka/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/kuka/0.1.0",
)
```


## Citation

@article{kalashnikov2018qt,
  title={Qt-opt: Scalable deep reinforcement learning for vision-based robotic manipulation},
  author={Kalashnikov, Dmitry and Irpan, Alex and Pastor, Peter and Ibarz, Julian and Herzog, Alexander and Jang, Eric and Quillen, Deirdre and Holly, Ethan and Kalakrishnan, Mrinal and Vanhoucke, Vincent and others},
  journal={arXiv preprint arXiv:1806.10293},
  year={2018}
}