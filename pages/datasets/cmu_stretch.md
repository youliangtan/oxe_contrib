# CMU Stretch

Robot interacting with different household environments.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Hello_Stretch](oed-playground/tree/master/pages/tags/Robot:Hello_Stretch.md), [Mobile_Manipulator](oed-playground/tree/master/pages/tags/Mobile_Manipulator.md), [Expert_Policy](oed-playground/tree/master/pages/tags/Expert_Policy.md), [Scene:Kitchen](oed-playground/tree/master/pages/tags/Scene:Kitchen.md), [Scene:Other_Household_environments](oed-playground/tree/master/pages/tags/Scene:Other_Household_environments.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/cmu_stretch/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/cmu_stretch/0.1.0",
)
```


## Citation

@inproceedings{bahl2023affordances,
  title={Affordances from Human Videos as a Versatile Representation for Robotics},
  author={Bahl, Shikhar and Mendonca, Russell and Chen, Lili and Jain, Unnat and Pathak, Deepak},
  booktitle={CVPR},
  year={2023}
}
@article{mendonca2023structured,
  title={Structured World Models from Human Videos},
  author={Mendonca, Russell and Bahl, Shikhar and Pathak, Deepak},
  journal={CoRL},
  year={2023}
}