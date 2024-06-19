import yaml
from typing import List, Union, Optional
from dataclasses import dataclass, field, asdict

@dataclass
class Dataset:
    dataset_name: str
    paper_title: str
    description: str
    tag: List[str]
    authors: List[str]
    citation: str
    download: List[dict]
    curation: List[dict]
    schema: List[dict]
    intended_level_of_support: int
    copyright: str

    @staticmethod
    def from_yaml(file_path: str) -> 'Dataset':
        """Reads the configuration from a YAML file and returns a Config object."""
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return Dataset(**data)
    
    def to_yaml(self, file_path: str):
        """Writes the Config object to a YAML file."""
        with open(file_path, 'w') as file:
            yaml.safe_dump(asdict(self), file, default_flow_style=False)
    
    def validate(self) -> bool:
        """Validates the configuration data according to the schema."""
        # Example validation rules, these can be extended based on requirements
        if not isinstance(self.dataset_name, str):
            raise ValueError("dataset_name must be a string.")
        if not isinstance(self.paper_title, str):
            raise ValueError("paper_title must be a string.")
        if not isinstance(self.intended_level_of_support, int):
            raise ValueError("intended_level_of_support must be an integer.")
        
        # Validate 'tag' as a list of strings
        if not all(isinstance(tag, str) for tag in self.tag):
            raise ValueError("Each tag must be a string.")
        
        # Add more validation rules as per the schema requirements
        return True

# Example usage
if __name__ == "__main__":
    config_path = 'config.yaml'
    
    # Reading and validating the config file
    config = Dataset.from_yaml(config_path)
    try:
        if config.validate():
            print("Configuration is valid.")
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Writing the config file back to YAML
    config.to_yaml('new_config.yaml')
