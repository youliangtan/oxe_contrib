# Berkeley Bridge

The robot interacts with household environments including kitchens, sinks, and tabletops. Skills include object rearrangement, sweeping, stacking, folding, and opening/closing doors and drawers. 

**Tags**: [Open-X-Embodiment](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Open-X-Embodiment.md), [Robot:WidowX](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Robot:WidowX.md), [Single_Arm](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Single_Arm.md), [Human_VR](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Human_VR.md), [Scene:Table_Top](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Table_Top.md), [Scene:Kitchen](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Kitchen.md), [Scene:Other_Household_environments](https://github.com/youliangtan/oxe_contrib/tree/main/pages/tags/Scene:Other_Household_environments.md)

## Sampled Visualization



## Download


```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="gs://gresearch/robotics/bridge/0.1.0")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="gs://gresearch/robotics/bridge/0.1.0",
)
```


## Citation

@inproceedings{walke2023bridgedata,
    title={BridgeData V2: A Dataset for Robot Learning at Scale},
    author={Walke, Homer and Black, Kevin and Lee, Abraham and Kim, Moo Jin and Du, Max and Zheng, Chongyi and Zhao, Tony and Hansen-Estruch, Philippe and Vuong, Quan and He, Andre and Myers, Vivek and Fang, Kuan and Finn, Chelsea and Levine, Sergey},
    booktitle={Conference on Robot Learning (CoRL)},
    year={2023}
}