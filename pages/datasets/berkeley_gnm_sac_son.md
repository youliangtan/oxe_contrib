# SACSoN

Mobile robot navigates pedestrian-rich environments (e.g. offices, school buildings etc.) and runs a learned policy that may interact with the pedestrians.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:TurtleBot_2](oed-playground/tree/master/pages/tags/Robot:TurtleBot_2.md), [Wheeled_Robot](oed-playground/tree/master/pages/tags/Wheeled_Robot.md), [Expert_Policy](oed-playground/tree/master/pages/tags/Expert_Policy.md), [Scene:Hallways](oed-playground/tree/master/pages/tags/Scene:Hallways.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/berkeley_gnm_sac_son/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/berkeley_gnm_sac_son/0.1.0",
)
```


## Citation

@article{hirose2023sacson,
  title={SACSoN: Scalable Autonomous Data Collection for Social Navigation},
  author={Hirose, Noriaki and Shah, Dhruv and Sridhar, Ajay and Levine, Sergey},
  journal={arXiv preprint arXiv:2306.01874},
  year={2023}
}