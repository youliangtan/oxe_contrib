import datetime
import yaml
import os
import pandas as pd


def create_readme(template_path, output_path, replacements):
    with open(template_path, 'r') as file:
        content = file.read()
        
    for key, value in replacements.items():
        placeholder = "{" + key + "}"
        content = content.replace(placeholder, value)
    
    with open(output_path, 'w') as file:
        file.write(content)


def generate_table_from_dataset_yamls(yaml_dir):
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
        "dataset_name", "tag", "description", 
        "download",
        "number_of_trajectories",
    ]

    # Ensure all specified columns are present in the DataFrame
    for col in columns:
        if col not in df.columns:
            df[col] = None  # Add missing columns with None values

    # Create the Markdown table
    markdown_table = df[columns].to_markdown(index=False)

    return markdown_table

def generate_readme():
    replacements = {
        "dataset_table": generate_table_from_dataset_yamls(yaml_directory)
    }

    create_readme(template_path = "./templates/index.md", 
                  output_path = "./README.md", 
                  replacements = replacements)


if __name__ == "__main__":
    yaml_directory = 'datasets'
    output_readme = 'README.md'
    generate_readme()
