# [Freiburg_Franka_Play](././pages/datasets/taco_p.md)

"The robot interacts with toy blocks, it pick and places them, stacks them, unstacks them, opens drawers, sliding doors and turrns on LED lights by pushing buttons."

**Tags**: 

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/taco_play/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/taco_play/0.1.0",
)
```


## Citation

@inproceedings{rosete2022tacorl,
author = {Erick Rosete-Beas and Oier Mees and Gabriel Kalweit and Joschka Boedecker and Wolfram Burgard},
title = {Latent Plans for Task Agnostic Offline Reinforcement Learning},
journal = {Proceedings of the 6th Conference on Robot Learning (CoRL)},
year = {2022}
}
@inproceedings{mees23hulc2,
title={Grounding  Language  with  Visual  Affordances  over  Unstructured  Data},
author={Oier Mees and Jessica Borja-Diaz and Wolfram Burgard},
booktitle = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
year={2023},
address = {London, UK}
}