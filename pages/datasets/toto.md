# TOTO Benchmark

The TOTO Benchmark Dataset contains trajectories of two tasks: scooping and pouring. For scooping, the objective is to scoop material from a bowl into the spoon. For pouring, the goal is to pour some material into a target cup on the table. 

**Tags**: [Open-X-Embodiment](oed-playground/tree/master/pages/tags/Open-X-Embodiment.md), [Robot:Franka](oed-playground/tree/master/pages/tags/Robot:Franka.md), [Single_Arm](oed-playground/tree/master/pages/tags/Single_Arm.md), [The_dataset_is_collected_in_3_ways:_Human_teleoperation_--_VR_Teleop,_trained_state-based_BC_policies,_and_trajectory_replay_with_noise](oed-playground/tree/master/pages/tags/The_dataset_is_collected_in_3_ways:_Human_teleoperation_--_VR_Teleop,_trained_state-based_BC_policies,_and_trajectory_replay_with_noise.md), [Scene:Table_Top](oed-playground/tree/master/pages/tags/Scene:Table_Top.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/toto/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/toto/0.1.0",
)
```


## Citation

@inproceedings{zhou2023train,
  author={Zhou, Gaoyue and Dean, Victoria and Srirama, Mohan Kumar and Rajeswaran, Aravind and Pari, Jyothish and Hatch, Kyle and Jain, Aryan and Yu, Tianhe and Abbeel, Pieter and Pinto, Lerrel and Finn, Chelsea and Gupta, Abhinav},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)}, 
  title={Train Offline, Test Online: A Real Robot Learning Benchmark}, 
  year={2023},
 }