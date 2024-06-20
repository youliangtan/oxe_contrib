# [Saytap](././pages/datasets/utokyo_saytap_converted_externally_to_rlds.md)

A Unitree Go1 robot follows human command in natural language (e.g., "trot forward slowly")

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/utokyo_saytap_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/utokyo_saytap_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{saytap2023,
  author = {Yujin Tang and Wenhao Yu and Jie Tan and Heiga Zen and Aleksandra Faust and
Tatsuya Harada},
  title  = {SayTap: Language to Quadrupedal Locomotion},
  eprint = {arXiv:2306.07580},
  url    = {https://saytap.github.io},
  note   = "{https://saytap.github.io}",
  year   = {2023}
}