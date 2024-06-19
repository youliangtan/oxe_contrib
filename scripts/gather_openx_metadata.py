from dataclasses import dataclass, field
from typing import List, Union, Optional
from pydantic import BaseModel, validator, ValidationError
import yaml

class ConfigSchema(BaseModel):
    dataset_name: str
    description: str
    tag: List[str]
    citation: str
    download: List[dict]
    link: str
    curation: List[dict]
    schema: List[dict]
    intended_level_of_support: int
    copyright: str
    number_of_trajectories: List[dict]
    size_in_gb: float
    version: str


    @validator('download', each_item=True)
    def validate_download_source(cls, value):
        if value.get('source') not in ['google_bucket', 'huggingface', 'google_drive']:
            raise ValueError(f"Invalid source: {value.get('source')}")
        return value

    @validator('schema', each_item=True)
    def validate_schema_feature_size(cls, value):
        if 'feature_size' in value and not isinstance(value['feature_size'], int):
            raise ValueError("feature_size must be an integer")
        return value

    @validator('intended_level_of_support', "number_of_trajectories")
    def validate_intended_level_of_support(cls, value):
        if not isinstance(value, int):
            raise ValueError("intended_level_of_support must be an integer")
        return value

    @validator('size_in_gb')
    def validate_intended_level_of_support(cls, value):
        if not isinstance(value, float):
            raise ValueError("intended_level_of_support must be an integer")
        return value
    
    @validator('tag', each_item=True)
    def validate_non_empty_strings(cls, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Items must be non-empty strings")
        return value

@dataclass
class Config:
    dataset_name: str
    description: str
    intended_level_of_support: int 
    copyright: str 
    size_in_gb: float
    version: str 
    citation: str = ""
    link: str = ""
    tag: List[str] = field(default_factory=list)
    download: List[dict] = field(default_factory=list)
    curation: List[dict] = field(default_factory=list)
    schema: List[dict] = field(default_factory=list)
    number_of_trajectories: List[dict] = field(default_factory=list)

    def to_yaml(self) -> str:
        return yaml.dump(self.__dict__)

    def validate(self) -> bool:
        try:
            ConfigSchema(**self.__dict__)
            return True
        except ValidationError as e:
            print("Validation Error:", e)
            return False



import numpy as np
import tensorflow_datasets as tfds

DATASETS = [
    'fractal20220817_data',
    'kuka',
    'bridge',
    'taco_play',
    'jaco_play',
    'berkeley_cable_routing',
    'roboturk',
    'nyu_door_opening_surprising_effectiveness',
    'viola',
    'berkeley_autolab_ur5',
    'toto',
    'language_table',
    'columbia_cairlab_pusht_real',
    'stanford_kuka_multimodal_dataset_converted_externally_to_rlds',
    'nyu_rot_dataset_converted_externally_to_rlds',
    'stanford_hydra_dataset_converted_externally_to_rlds',
    'austin_buds_dataset_converted_externally_to_rlds',
    'nyu_franka_play_dataset_converted_externally_to_rlds',
    'maniskill_dataset_converted_externally_to_rlds',
    'cmu_franka_exploration_dataset_converted_externally_to_rlds',
    'ucsd_kitchen_dataset_converted_externally_to_rlds',
    'ucsd_pick_and_place_dataset_converted_externally_to_rlds',
    'austin_sailor_dataset_converted_externally_to_rlds',
    'austin_sirius_dataset_converted_externally_to_rlds',
    'bc_z',
    'usc_cloth_sim_converted_externally_to_rlds',
    'utokyo_pr2_opening_fridge_converted_externally_to_rlds',
    'utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds',
    'utokyo_saytap_converted_externally_to_rlds',
    'utokyo_xarm_pick_and_place_converted_externally_to_rlds',
    'utokyo_xarm_bimanual_converted_externally_to_rlds',
    'robo_net',
    'berkeley_mvp_converted_externally_to_rlds',
    'berkeley_rpt_converted_externally_to_rlds',
    'kaist_nonprehensile_converted_externally_to_rlds',
    'stanford_mask_vit_converted_externally_to_rlds',
    'tokyo_u_lsmo_converted_externally_to_rlds',
    'dlr_sara_pour_converted_externally_to_rlds',
    'dlr_sara_grid_clamp_converted_externally_to_rlds',
    'dlr_edan_shared_control_converted_externally_to_rlds',
    'asu_table_top_converted_externally_to_rlds',
    'stanford_robocook_converted_externally_to_rlds',
    'eth_agent_affordances',
    'imperialcollege_sawyer_wrist_cam',
    'iamlab_cmu_pickup_insert_converted_externally_to_rlds',
    'uiuc_d3field',
    'utaustin_mutex',
    'berkeley_fanuc_manipulation',
    'cmu_play_fusion',
    'cmu_stretch',
    'berkeley_gnm_recon',
    'berkeley_gnm_cory_hall',
    'berkeley_gnm_sac_son'
]

def dataset2path(dataset_name):
  if dataset_name == 'robo_net':
    version = '1.0.0'
  elif dataset_name == 'language_table':
    version = '0.0.1'
  else:
    version = '0.1.0'
  return f'gs://gresearch/robotics/{dataset_name}/{version}'

dataset = 'fractal20220817_data'
b = tfds.builder_from_directory(builder_dir=dataset2path(dataset))

# Get the dataset info
info = b.info
print(info)

def from_open_x_to_config(
    ds_info: tfds.core.DatasetInfo,
):
    number_of_trajectories = [{split_name: ds_info.splits[split_name].num_examples} for split_name in ds_info.splits]
    config = Config(
        dataset_name=ds_info.name,
        version=str(ds_info.version),
        description=ds_info.description,
        tag=["open-x", "manipulation", "single-arm", "parallel-jaw-gripper"],
        citation=ds_info.citation,
        download=[{"source": "google_bucket", "link": f"gs://gresearch/robotics/{ds_info.name}/{ds_info.version}"}],
        curation=[{"open_x_embodiment": True}],
        number_of_trajectories= number_of_trajectories,
        size_in_gb= float(ds_info.dataset_size / 1e9),
        intended_level_of_support=4,
        copyright="Copyright",
        schema=[
            {"TODO": "schema_todo"}
        ],
        link="TODO",
    )
    return config

for dataset in DATASETS:
    b = tfds.builder_from_directory(builder_dir=dataset2path(dataset))
    info = b.info
    config = from_open_x_to_config(info)
    if config.validate():
        print(f"Config for {dataset} is valid")
    else:
        print(f"Config for {dataset} is invalid")
    
    yaml_output = config.to_yaml()
    with open(f"../datasets/{dataset}.yaml", "w") as f:
        f.write(yaml_output)
