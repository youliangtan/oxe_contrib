# Robonet

The robot interacts with the objects in a bin placed in front of it

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Multi-Robot](oed-playground/tree/master/pages/tags/Robot:Multi-Robot.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Scripted](oed-playground/tree/master/pages/tags/Scripted.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/robo_net/1.0.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/robo_net/1.0.0",
)
```


## Citation

@inproceedings{dasari2019robonet,
    title={RoboNet: Large-Scale Multi-Robot Learning},
    author={Sudeep Dasari and Frederik Ebert and Stephen Tian and Suraj Nair and Bernadette Bucher and Karl Schmeckpeper and Siddharth Singh and Sergey Levine and Chelsea Finn},
    year={2019},
    eprint={1910.11215},
    archivePrefix={arXiv},
    primaryClass={cs.RO},
    booktitle={CoRL 2019: Volume 100 Proceedings of Machine Learning Research}
}