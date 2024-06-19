import datetime


import yaml
import os
import pandas as pd

def generate_readme_from_yaml(yaml_dir):
    """
    Generate a README.md table from YAML files in the specified directory.

    Parameters:
    yaml_dir (str): The directory containing YAML files.
    """
    # List to hold all dataset information
    datasets = []

    # Iterate over all YAML files in the directory
    for filename in os.listdir(yaml_dir):
        if filename.endswith(".yaml"):
            file_path = os.path.join(yaml_dir, filename)
            with open(file_path, 'r') as file:
                # Load the YAML content
                dataset_info = yaml.safe_load(file)
                datasets.append(dataset_info)

    # Convert the list of datasets to a DataFrame for easy manipulation
    df = pd.DataFrame(datasets)
    
    # Define the columns we want to include in the Markdown table
    columns = [
        "dataset_name", "description", "tag",
        "download", "curation", 
        "intended_level_of_support", "copyright",
        "number_of_trajectories", "size_in_gb"
    ]

    # Ensure all specified columns are present in the DataFrame
    for col in columns:
        if col not in df.columns:
            df[col] = None  # Add missing columns with None values

    # Create the Markdown table
    markdown_table = df[columns].to_markdown(index=False)

    return markdown_table

def generate_readme():
    content = f"""
# Open Embodiment Datasets

This is an auto-generated README file at time {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Dataset 

{generate_readme_from_yaml(yaml_directory)}

## Contributing

Explain how to contribute here.
    """

    with open(output_readme, "w") as readme_file:
        readme_file.write(content)
        

if __name__ == "__main__":
    yaml_directory = 'datasets'
    output_readme = 'README.md'
    generate_readme()
