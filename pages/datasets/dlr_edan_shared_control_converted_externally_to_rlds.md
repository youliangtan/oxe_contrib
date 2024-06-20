# [DLR_Wheelchair_Shared_Control](././pages/datasets/dlr_edan_shared_control_converted_externally_to_rlds.md)

The robot grasps a set of different objects in a table top and a shelf. 

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/dlr_edan_shared_control_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/dlr_edan_shared_control_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{vogel_edan_2020,
        title = {EDAN - an EMG-Controlled Daily Assistant to Help People with Physical Disabilities},
        language = {en},
        booktitle = {2020 {IEEE}/{RSJ} {International} {Conference} on {Intelligent} {Robots} and {Systems} ({IROS})},
        author = {Vogel, Jörn and Hagengruber, Annette and Iskandar, Maged and Quere, Gabriel and Leipscher, Ulrike and Bustamante, Samuel and Dietrich, Alexander and Hoeppner, Hannes and Leidner, Daniel and Albu-Schäffer, Alin},
        year = {2020}
}
@inproceedings{quere_shared_2020,
        address = {Paris, France},
        title = {Shared {Control} {Templates} for {Assistive} {Robotics}},
        language = {en},
        booktitle = {2020 {IEEE} {International} {Conference} on {Robotics} and {Automation} ({ICRA})},
        author = {Quere, Gabriel and Hagengruber, Annette and Iskandar, Maged and Bustamante, Samuel and Leidner, Daniel and Stulp, Freek and Vogel, Joern},
        year = {2020},
        pages = {7},
}