# Stanford Kuka Multimodal

The robot learns to insert differently-shaped pegs into differently-shaped holes with low tolerances (~2mm).

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Kuka_iiwa](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Kuka_iiwa.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Expert_Policy](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Expert_Policy.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/stanford_kuka_multimodal_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/stanford_kuka_multimodal_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{lee2019icra,
  title={Making sense of vision and touch: Self-supervised learning of multimodal representations for contact-rich tasks},
  author={Lee, Michelle A and Zhu, Yuke and Srinivasan, Krishnan and Shah, Parth and Savarese, Silvio and Fei-Fei, Li and  Garg, Animesh and Bohg, Jeannette},
  booktitle={2019 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2019},
  url={https://arxiv.org/abs/1810.10191}
}