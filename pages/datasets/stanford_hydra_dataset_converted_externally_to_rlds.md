# Stanford HYDRA

The robot performs the following tasks in corresponding environment: making a cup of coffee using the keurig machine; making a toast using the oven; sorting dishes onto the dish rack.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Human_VR](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Human_VR.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md), [Scene:Kitchen](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Kitchen.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/stanford_hydra_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/stanford_hydra_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{belkhale2023hydra,
 title={HYDRA: Hybrid Robot Actions for Imitation Learning},
 author={Belkhale, Suneel and Cui, Yuchen and Sadigh, Dorsa},
 journal={arxiv},
 year={2023}
}