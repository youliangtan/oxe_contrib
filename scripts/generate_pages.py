import datetime
import yaml
import os
import pandas as pd


DATASET_DIR = "./datasets"
OUTPUT_TAG_PAGE_DIR = "./pages/tags"
OUTPUT_DATASET_PAGE_DIR = "./pages/datasets"
URL_DATASET_PAGE_DIR = "oed-playground/tree/master/pages/datasets"
URL_TAG_PAGE_DIR = "oed-playground/tree/master/pages/tags"
TEMPLATE_DIR = "pages/templates"


def dataset_name_to_url_string(dataset_name, dataset_path_name):
    """
    Convert dataset name to a markdown link.
    dataset_name (str): the rendered dataset name (example: "Berkeley Cable Routing")
    dataset_path_name (str): the dataset path (example: "berkeley_cable_routing")
    """
    dataset_name = dataset_name.replace(" ", "_")
    return f"[{dataset_name}]({URL_DATASET_PAGE_DIR}/{dataset_path_name}.md)"
    

def tag_list_to_url_string(tag_list):
    # convert tag to a markdown link
    str = ""
    for tag in tag_list:
        no_space_tag = tag.replace(" ", "_")
        str += f"[{no_space_tag}]({URL_TAG_PAGE_DIR}/{no_space_tag}.md)"
        if tag != tag_list[-1]:
            str += ", "
    return str


template_download_from_google_bucket = """
```python
# Method 1: 
import tensorflow_datasets as tfds
tfds.builder_from_directory(builder_dir="{download_link}")
ds = b.as_dataset(split='train[:10]')

# Method 2:
import fog_x
dataset = fog_x.Dataset(
    name="demo_ds",
    path="~/test_dataset", # can be AWS S3, other Google Bucket
)  

dataset.load_rtx_episodes(
    name="{download_link}",
)
```
"""
def download_list_to_download_method(download_list):
    for download in download_list:
        if download["source"] == "google_bucket":
            return template_download_from_google_bucket.format(download_link=download["link"])
        else:
            raise ValueError("Unknown download source")
    return ""


def create_readme(template_path, output_path, replacements):
    with open(template_path, 'r') as file:
        content = file.read()
        
    for key, value in replacements.items():
        placeholder = "{" + key + "}"
        content = content.replace(placeholder, value)
    
    with open(output_path, 'w') as file:
        file.write(content)


def generate_table_from_dataset_yamls():
    """
    Generate a README.md table from YAML files in the specified directory.
    """
    # List to hold all dataset information
    datasets = []

    # Iterate over all YAML files in the directory
    for filename in os.listdir(DATASET_DIR):
        if filename.endswith(".yaml"):
            file_path = os.path.join(DATASET_DIR, filename)
            with open(file_path, 'r') as file:
                # Load the YAML content
                dataset_info = yaml.safe_load(file)
                datasets.append(dataset_info)

    # Convert the list of datasets to a DataFrame for easy manipulation
    df = pd.DataFrame(datasets)
    
    # Define the columns we want to include in the Markdown table
    columns = [
        "dataset_name", "tag", "description", 
    ]
    
    
    # Ensure all specified columns are present in the DataFrame
    for col in columns:
        if col not in df.columns:
            df[col] = None  # Add missing columns with None values
    
    # convert dataset_name to a markdown link
    # df["dataset_name"] = df["dataset_name"].apply(dataset_name_to_url_string)
    df["dataset_name"] = df.apply(lambda x: dataset_name_to_url_string(x["dataset_name"], x["dataset_file_name"]), axis=1)

    # convert tag to a markdown link
    df["tag"] = df["tag"].apply(tag_list_to_url_string)

    # re-order rows by level_of_support and dataset_name
    # descending by level_of_support
    # ascending by dataset_name
    df = df.sort_values(by=["level_of_support", "dataset_name"], ascending=[False, True])

    df = df[columns]

    # rename column names 
    df = df.rename(columns={
        "dataset_name": "Dataset",
        "tag": "Tags",
        "description": "Description",
    })
    # Create the Markdown table
    markdown_table = df.to_markdown(index=False)

    return markdown_table

def generate_project_pages():
    for filename in os.listdir(DATASET_DIR):
        file_path = os.path.join(DATASET_DIR, filename)
        dataset_path_name = filename.strip(".yaml")
        with open(file_path, 'r') as file:
            dataset_info = yaml.safe_load(file)

        tags = tag_list_to_url_string(dataset_info.get("tag", ""))
        description = dataset_info.get("description", "")
        download = download_list_to_download_method(dataset_info.get("download", ""))
        visualization = dataset_info.get("visualization", "")
        citation = dataset_info.get("citation", "")

        replacements = {
            "dataset_name": dataset_info.get("dataset_name", ""),
            "tags": tags,
            "description": description,
            "download": download,
            "visualization": visualization,
            "citation": citation,
        }

        create_readme(template_path = f"{TEMPLATE_DIR}/dataset.md", 
                      output_path = "./pages/datasets/{}.md".format(dataset_path_name), 
                      replacements = replacements)
    

def generate_index_page():
    replacements = {
        "dataset_table": generate_table_from_dataset_yamls()
    }

    create_readme(template_path = f"{TEMPLATE_DIR}/index.md", 
                  output_path = "./README.md", 
                  replacements = replacements)


def generate_tag_page():
    tag_pages = {}
    for filename in os.listdir(DATASET_DIR):
        file_path = os.path.join(DATASET_DIR, filename)
        with open(file_path, 'r') as file:
            dataset_info = yaml.safe_load(file)
        
        tags = dataset_info.get("tag", [])
        dataset_name = dataset_info.get("dataset_name", "")
        dataset_description = dataset_info.get("description", "")
        dataset_path_name = filename.strip(".yaml")
        for tag in tags:
            no_space_tag = tag.replace(" ", "_")
            tag_file_path = f"{OUTPUT_TAG_PAGE_DIR}/{no_space_tag}.md"
            if tag_file_path not in tag_pages:
                tag_pages[tag_file_path] = []
            ds_record = f"- {dataset_name_to_url_string(dataset_name, dataset_path_name)}: {dataset_description}"
            tag_pages[tag_file_path].append(ds_record)

    for tag_file_path, datasets in tag_pages.items():
        # use the template
        with open(f"{TEMPLATE_DIR}/tag.md", 'r') as file:
            content = file.read()
        tag = os.path.basename(tag_file_path).replace(".md", "")

        content = content.replace("{tag}", tag)
        content = content.replace("{tag_list}", "\n".join(datasets))
        with open(tag_file_path, 'w') as file:
            file.write(content)


if __name__ == "__main__":
    generate_index_page()
    generate_project_pages()
    generate_tag_page()
