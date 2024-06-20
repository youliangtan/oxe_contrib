# [LSMO_Dataset](././pages/datasets/tokyo_u_lsmo_converted_externally_to_rlds.md)

The robot avoids obstacle on the table and reaches the target object.

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/tokyo_u_lsmo_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/tokyo_u_lsmo_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@Article{Osa22,
  author  = {Takayuki Osa},
  journal = {The International Journal of Robotics Research},
  title   = {Motion Planning by Learning the Solution Manifold in Trajectory Optimization},
  year    = {2022},
  number  = {3},
  pages   = {291--311},
  volume  = {41},
}