# Columbia PushT Dataset

The robot pushes a T-shaped block into a fixed goal pose, and then move to an fixed exit zone.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:UR5](oed-playground/tree/master/pages/tags/Robot:UR5.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Human_VR](oed-playground/tree/master/pages/tags/Human_VR.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/columbia_cairlab_pusht_real/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/columbia_cairlab_pusht_real/0.1.0",
)
```


## Citation

@inproceedings{chi2023diffusionpolicy,
	title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
	author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
	booktitle={Proceedings of Robotics: Science and Systems (RSS)},
	year={2023}
}