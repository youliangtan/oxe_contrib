# USC Jaco Play

The robot performs pick-place tasks in a tabletop toy kitchen environment. Some examples of the task include, "Pick up the orange fruit.", "Put the black bowl in the sink."

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Jaco_2](oed-playground/tree/master/pages/tags/Robot:Jaco_2.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Human_VR](oed-playground/tree/master/pages/tags/Human_VR.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md), [Scene:Kitchen](oed-playground/tree/master/pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/jaco_play/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/jaco_play/0.1.0",
)
```


## Citation

@software{dass2023jacoplay,
  author = {Dass, Shivin and Yapeter, Jullian and Zhang, Jesse and Zhang, Jiahui
            and Pertsch, Karl and Nikolaidis, Stefanos and Lim, Joseph J.},
  title = {CLVR Jaco Play Dataset},
  url = {https://github.com/clvrai/clvr_jaco_play_dataset},
  version = {1.0.0},
  year = {2023}
}