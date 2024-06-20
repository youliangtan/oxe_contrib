# Berkeley RPT Data

Picking, stacking, destacking, and bin picking with variations in objects.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Franka](oed-playground/tree/master/pages/tags/Robot:Franka.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Scripted](oed-playground/tree/master/pages/tags/Scripted.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/berkeley_rpt_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/berkeley_rpt_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@article{Radosavovic2023,
  title={Robot Learning with Sensorimotor Pre-training},
  author={Ilija Radosavovic and Baifeng Shi and Letian Fu and Ken Goldberg and Trevor Darrell and Jitendra Malik},
  year={2023},
  journal={arXiv:2306.10007}
}
