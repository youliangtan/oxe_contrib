from dataclasses import dataclass, field
from typing import List, Union, Optional
from pydantic import BaseModel, validator, ValidationError
import yaml
import numpy as np
import tensorflow_datasets as tfds
import pandas as pd

class ConfigSchema(BaseModel):
    dataset_name: str
    dataset_file_name: str
    description: str
    tag: List[str]
    citation: str
    download: List[dict]
    link: str
    curation: List[dict]
    schema: List[dict]
    level_of_support: int
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

    @validator('level_of_support', "number_of_trajectories")
    def validate_level_of_support(cls, value):
        if not isinstance(value, int):
            raise ValueError("level_of_support must be an integer")
        return value

    @validator('size_in_gb')
    def validate_level_of_support(cls, value):
        if not isinstance(value, float):
            raise ValueError("level_of_support must be an integer")
        return value
    
    @validator('tag', each_item=True)
    def validate_non_empty_strings(cls, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Items must be non-empty strings")
        return value

@dataclass
class Config:
    dataset_name: str
    dataset_file_name: str
    description: str
    level_of_support: int 
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



def dataset2path(dataset_name):
  if dataset_name == 'robo_net':
    version = '1.0.0'
  elif dataset_name == 'language_table':
    version = '0.0.1'
  else:
    version = '0.1.0'
  return f'gs://gresearch/robotics/{dataset_name}/{version}'

# file_path = "scripts/open-x/Open X-Embodiment Dataset Overview - Dataset Overview.csv"

# This is manually downloaded from the oxe website:
# https://docs.google.com/spreadsheets/d/1rPBD77tk60AEIGZrGSODwyyzs5FgCU9Uz3h-3_t2A9g/edit?gid=0#gid=0
# and removed the top 15 lines
file_path = "docs/oxe_data_24jul2024.csv"

with open(file_path, "r") as f:
    # remove the first 15 lines and read as csv
    # df = pd.read_csv(f, skiprows=14)
    df = pd.read_csv(f)
    print(df.columns)

# iterate over df
for i, row in df.iterrows():
    dataset_name = row["Registered Dataset Name"]
    try:
        ds_info = tfds.builder_from_directory(builder_dir=dataset2path(dataset_name)).info
        version = str(ds_info.version)
        download = [{"source": "google_bucket", "link": f"gs://gresearch/robotics/{ds_info.name}/{ds_info.version}"}]
        level_of_support = 4
    except:
        version = "0.0.0"
        download = []
        level_of_support = 0
        dataset_name = row["Dataset"].replace(" ", "_").lower()
    number_of_trajectories = [{split_name: ds_info.splits[split_name].num_examples} for split_name in ds_info.splits]
    
    tags = ["Open-X-Embodiment"]
    if row["Robot"] and str(row["Robot"]) != "nan":
        tags.append("Robot:" + row["Robot"])
    if row["Robot Morphology"] and str(row["Robot Morphology"]) != "nan":
        tags.append(row["Robot Morphology"])
    if row["Data Collect Method"] and str(row["Data Collect Method"]) != "nan":
        tags.append(row["Data Collect Method"])
    if row["Scene Type"] and str(row["Scene Type"]) != "nan":
        for tag in row["Scene Type"].strip().split(","):
            if "Kitchen" in tag:
                tag = 'Kitchen'
            tags.append("Scene:" + tag.strip())

    print(tags)
    
    config = Config(
        dataset_name= row['Dataset'],
        dataset_file_name= dataset_name,
        version= version,
        description= row['Description'],
        tag=tags,
        citation=row['Citation'],
        download=download,
        curation=[{"open_x_embodiment": True}],
        number_of_trajectories= number_of_trajectories,
        size_in_gb= row["File Size (GB)"],
        level_of_support=level_of_support,
        copyright="Copyright",
        schema=[
            {"TODO": "schema_todo"}
        ],
        link="TODO",
    )

    if config.validate():
        print(f"Config for {dataset_name} is valid")       
        yaml_output = config.to_yaml()
        with open(f"./datasets/{dataset_name}.yaml", "w") as f:
            f.write(yaml_output)
    else:
        print(f"Config for {dataset_name} is invalid")
        print(config)

