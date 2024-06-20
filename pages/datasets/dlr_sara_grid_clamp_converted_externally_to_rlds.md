# DLR Sara Grid Clamp Dataset

The robot learns to place the grid clamp in the grids on the table.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:DLR_SARA](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:DLR_SARA.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Expert_Policy](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Expert_Policy.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md), [Scene:Workshop_environment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Workshop_environment.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/dlr_sara_grid_clamp_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/dlr_sara_grid_clamp_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{padalkar2023guided,
  title={A guided reinforcement learning approach using shared control templates for learning manipulation skills in the real world},
  author={Padalkar, Abhishek and Quere, Gabriel and Raffin, Antonin and Silv{\'e}rio, Jo{\~a}o and Stulp, Freek},
  journal={Research square preprint rs-3289569/v1},
  year={2023}
}