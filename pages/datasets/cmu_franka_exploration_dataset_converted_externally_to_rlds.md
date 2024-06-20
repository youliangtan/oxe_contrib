# CMU Franka Exploration

Franka exploring kitchen environment, lifting knife and vegetable and opening cabinet.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Expert_Policy](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Expert_Policy.md), [Scene:Kitchen](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/cmu_franka_exploration_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/cmu_franka_exploration_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{mendonca2023structured,
              title={Structured World Models from Human Videos},
              author={Mendonca, Russell  and Bahl, Shikhar and Pathak, Deepak},
              journal={RSS},
              year={2023}
            }