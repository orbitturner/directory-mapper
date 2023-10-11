# arborescence_util.py
import os
import json
import re
from loguru import logger
import yaml

file_identifier = "File"


def draw_directory_structure(folder, prefix="", ignore_folders=None, ignore_regex=None):
    # Get the list of items in the folder
    elements = os.listdir(folder)

    # Iterate through the items
    for i, element in enumerate(elements):
        full_path = os.path.join(folder, element)
        is_last = i == len(elements) - 1

        # Ignore specified folders
        if ignore_folders and element in ignore_folders:
            continue

        # Ignore folders matching the regex pattern
        if ignore_regex and re.match(ignore_regex, element):
            continue

        # Display the prefix
        if is_last:
            print(prefix + "└── " + element)
        else:
            print(prefix + "├── " + element)

        # If the item is a folder, recursively display its contents
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            draw_directory_structure(full_path, new_prefix, ignore_folders, ignore_regex)


def display_directory_format(folder_path, format, ignore_folders=None, ignore_regex=None):
    if format == "json":
        directory_json = generate_directory_json(folder_path, ignore_folders, ignore_regex)
        print(json.dumps(directory_json, indent=2))
    elif format == "yaml":
        directory_yaml = generate_directory_yaml(folder_path, ignore_folders, ignore_regex)
        print(yaml.dump(directory_yaml, default_flow_style=False))


def generate_directory_json(folder, ignore_folders=None, ignore_regex=None):
    directory = {}
    elements = os.listdir(folder)

    for element in elements:
        full_path = os.path.join(folder, element)

        # Ignore specified folders
        if ignore_folders and element in ignore_folders:
            continue

        # Ignore folders matching the regex pattern
        if ignore_regex and re.match(ignore_regex, element):
            continue

        if os.path.isdir(full_path):
            directory[element] = generate_directory_json(full_path, ignore_folders, ignore_regex)
        else:
            directory[element] = file_identifier
    logger.debug(f"📂 Directory JSON: {directory}")
    return directory


def generate_directory_yaml(folder, ignore_folders=None, ignore_regex=None):
    directory = {}
    elements = os.listdir(folder)

    for element in elements:
        full_path = os.path.join(folder, element)

        # Ignore specified folders
        if ignore_folders and element in ignore_folders:
            continue

        # Ignore folders matching the regex pattern
        if ignore_regex and re.match(ignore_regex, element):
            continue

        if os.path.isdir(full_path):
            directory[element] = generate_directory_yaml(full_path, ignore_folders, ignore_regex)
        else:
            directory[element] = file_identifier
    # log directly into the logfile without printing to the console
    logger.debug(f"📂 Directory YAML: {directory}")
    return directory


def create_directory(description_json, folder_path, ignore_folders=None, ignore_regex=None):
    try:
        # Load the JSON description
        with open(description_json, 'r') as file:
            description = json.load(file)
            logger.debug(f"📂 Description to Create: {description}")

        # Create the directory
        for name, content in description.items():
            # Ignore specified folders
            if ignore_folders and name in ignore_folders:
                continue

            # Ignore folders matching the regex pattern
            if ignore_regex and re.match(ignore_regex, name):
                continue

            element_path = os.path.join(folder_path, name)

            if isinstance(content, dict):
                # If the value is a dictionary, recursively create the folder
                os.makedirs(element_path, exist_ok=True)
                logger.info(f"📂 Folder created: {element_path}")
                create_directory(description[name], element_path, ignore_folders, ignore_regex)
            elif content == "File":
                # If the value is "File", create the file
                with open(element_path, 'w') as file:
                    file.write("")  # You can add content if needed
                logger.info(f"✅ File created: {element_path}")
            else:
                logger.warning(f"⚠️ Unrecognized value for {name}: {content}")

        logger.info("✅ Directory successfully created from the JSON description.")

    except Exception as e:
        logger.error(f"❌ An error occurred while creating the directory: {e}")
