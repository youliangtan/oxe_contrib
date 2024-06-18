import datetime

def generate_readme():
    content = f"""
    # Project Title

    This is an auto-generated README file.

    ## Date of Generation

    {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    ## Introduction

    Describe your project here.

    ## Usage

    Provide usage instructions here.

    ## Contributing

    Explain how to contribute here.
    """

    with open("README.md", "w") as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    generate_readme()
