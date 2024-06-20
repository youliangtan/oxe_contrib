# Furniture Bench

The robot assembles one of 9 3D-printed furniture models on the table, which requires grasping, inserting, and screwing.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Human_VR](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Human_VR.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/furniture_bench_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/furniture_bench_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{heo2023furniturebench,
  title={FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation},
  author={Minho Heo and Youngwoon Lee and Doohyun Lee and Joseph J. Lim},
  booktitle={Robotics: Science and Systems},
  year={2023}
}