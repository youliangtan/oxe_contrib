# DLR Sara Pour Dataset

The robot learns to pour ping-pong balls from a cup held in the end-effector into the cup placed on the table.

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:DLR_SARA](oed-playground/tree/master/pages/tags/Robot:DLR_SARA.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [Expert_Policy](oed-playground/tree/master/pages/tags/Expert_Policy.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md), [Scene:Household_objects](oed-playground/tree/master/pages/tags/Scene:Household_objects.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/dlr_sara_pour_converted_externally_to_rlds/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/dlr_sara_pour_converted_externally_to_rlds/0.1.0",
)
```


## Citation

@inproceedings{padalkar2023guiding,
  title={Guiding Reinforcement Learning with Shared Control Templates},
  author={Padalkar, Abhishek and Quere, Gabriel and Steinmetz, Franz and Raffin, Antonin and Nieuwenhuisen, Matthias and Silv{\'e}rio, Jo{\~a}o and Stulp, Freek},
  booktitle={40th IEEE International Conference on Robotics and Automation, ICRA 2023},
  year={2023},
  organization={IEEE}
}