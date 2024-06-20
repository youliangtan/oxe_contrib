# UIUC D3Field

The robot completes tasks specified by the goal image, including organizing utensils, shoes, mugs.

**Tags**: [Open-X-Embodiment](./pages/tags/Open-X-Embodiment.md), [Robot:Kinova_Gen3](./pages/tags/Robot:Kinova_Gen3.md), [Single_Arm](./pages/tags/Single_Arm.md), [Scripted](./pages/tags/Scripted.md), [Scene:Table_Top](./pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/uiuc_d3field/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/uiuc_d3field/0.1.0",
)
```


## Citation

@article{wang2023d3field,
  title={D^3Field: Dynamic 3D Descriptor Fields for Generalizable Robotic Manipulation}, 
  author={Wang, Yixuan and Li, Zhuoran and Zhang, Mingtong and Driggs-Campbell, Katherine and Wu, Jiajun and Fei-Fei, Li and Li, Yunzhu},
  journal={arXiv preprint arXiv:},
  year={2023},
}