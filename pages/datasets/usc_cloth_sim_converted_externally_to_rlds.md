# USC Cloth Sim

The robot manipulates a deformable object (cloth on a tabletop) along a diagonal.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Franka](oed-playground/tree/master/pages/tags/Robot:Franka.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Scripted](oed-playground/tree/master/pages/tags/Scripted.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md), [Scene:Kitchen](oed-playground/tree/master/pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/usc_cloth_sim_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/usc_cloth_sim_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{salhotra2022dmfd,
    author={Salhotra, Gautam and Liu, I-Chun Arthur and Dominguez-Kuhne, Marcus and Sukhatme, Gaurav S.},
    journal={IEEE Robotics and Automation Letters},
    title={Learning Deformable Object Manipulation From Expert Demonstrations},
    year={2022},
    volume={7},
    number={4},
    pages={8775-8782},
    doi={10.1109/LRA.2022.3187843}
}