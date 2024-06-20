# UTokyo xArm Bimanual

The robots reach a towel on the table. They also unfold a wrinkled towel.

**Tags**: [Open-X-Embodiment](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:xArm_Bimanual](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Robot:xArm_Bimanual.md), [Bi-Manual](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Bi-Manual.md), [Human_Puppeteering](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Human_Puppeteering.md), [Scene:Table_Top](https://github.com/KeplerC/oed-playground/tree/main/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/utokyo_xarm_bimanual_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/utokyo_xarm_bimanual_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@misc{matsushima2023weblab,
  title={Weblab xArm Dataset},
  author={Tatsuya Matsushima and Hiroki Furuta and Yusuke Iwasawa and Yutaka Matsuo},
  year={2023},
}