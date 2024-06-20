# [NYU_VINN](././pages/datasets/nyu_door_opening_surprising_effectiveness.md)

The robot opens cabinet doors for a variety of cabinets.

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/nyu_door_opening_surprising_effectiveness/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/nyu_door_opening_surprising_effectiveness/0.1.0",
)
```


## Citation

@misc{pari2021surprising,
    title={The Surprising Effectiveness of Representation Learning for Visual Imitation}, 
    author={Jyothish Pari and Nur Muhammad Shafiullah and Sridhar Pandian Arunachalam and Lerrel Pinto},
    year={2021},
    eprint={2112.01511},
    archivePrefix={arXiv},
    primaryClass={cs.RO}
}