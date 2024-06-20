# Austin Sirius

The dataset comprises two tasks, kcup and gear. The kcup task requires opening the kcup holder, inserting the kcup into the holder, and closing the holder. The gear task requires inserting the blue gear onto the right peg, followed by inserting the smaller red gear.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:Franka](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:Franka.md), [Single_Arm](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Single_Arm.md), [Human_Spacemouse](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Human_Spacemouse.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/austin_sirius_dataset_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/austin_sirius_dataset_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{liu2022robot,
    title = {Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During Deployment},
    author = {Huihan Liu and Soroush Nasiriany and Lance Zhang and Zhiyao Bao and Yuke Zhu},
    booktitle = {Robotics: Science and Systems (RSS)},
    year = {2023}
}