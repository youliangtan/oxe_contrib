# ASU TableTop Manipulation

The robot interacts with a few objects on a table. It picks up, pushes forward, or rotates the objects.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:UR5](oed-playground/tree/master/pages/tags/Robot:UR5.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Scripted](oed-playground/tree/master/pages/tags/Scripted.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/asu_table_top_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/asu_table_top_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{zhou2023modularity,
  title={Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation},
  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Stepputtis, Simon and Amor, Heni},
  booktitle={Conference on Robot Learning},
  pages={1684--1695},
  year={2023},
  organization={PMLR}
}
@article{zhou2023learning,
  title={Learning modular language-conditioned robot policies through attention},
  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Ben Amor, Heni and Stepputtis, Simon},
  journal={Autonomous Robots},
  pages={1--21},
  year={2023},
  publisher={Springer}
}