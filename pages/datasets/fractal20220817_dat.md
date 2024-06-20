# [RT-1_Robot_Action](././pages/datasets/fractal20220817_dat.md)

Robot picks, places and moves 17 objects from the google micro kitchens.

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/fractal20220817_data/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/fractal20220817_data/0.1.0",
)
```


## Citation

@article{brohan2022rt,
  title={Rt-1: Robotics transformer for real-world control at scale},
  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Dabis, Joseph and Finn, Chelsea and Gopalakrishnan, Keerthana and Hausman, Karol and Herzog, Alex and Hsu, Jasmine and others},
  journal={arXiv preprint arXiv:2212.06817},
  year={2022}
}