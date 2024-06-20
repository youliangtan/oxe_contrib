# Austin Mutex

The Mutex dataset involves a diverse range of tasks in a home environment, encompassing pick and place tasks like "putting bread on a plate," as well as contact-rich tasks such as "opening an air fryer and putting a bowl with dogs in it" or "taking out a tray from the oven and placing bread on it."

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Human_Spacemouse](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Human_Spacemouse.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/utaustin_mutex/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/utaustin_mutex/0.1.0",
)
```


## Citation

@inproceedings{shah2023mutex,
    title={{MUTEX}: Learning Unified Policies from Multimodal Task Specifications},
    author={Rutav Shah and Roberto Mart{\'\i}n-Mart{\'\i}n and Yuke Zhu},
    booktitle={7th Annual Conference on Robot Learning},
    year={2023},
    url={https://openreview.net/forum?id=PwqiqaaEzJ}
}