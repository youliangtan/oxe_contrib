# [Tokyo_PR2_Tabletop_Manipulation](././pages/datasets/utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds.md)

The PR2 robot conducts manipulation for table top object. It conducts pick-and-place of bread and grape and folds cloth.

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@misc{oh2023pr2utokyodatasets,
  author={Jihoon Oh and Naoaki Kanazawa and Kento Kawaharazuka},
  title={X-Embodiment U-Tokyo PR2 Datasets},
  year={2023},
  url={https://github.com/ojh6404/rlds_dataset_builder},
}