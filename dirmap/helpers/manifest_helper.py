import os
import json

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Local manifest.json path
LOCAL_MANIFEST_PATH = os.path.join(current_dir, '..', 'manifest.json')


def get_current_version():
    """
    Get the current version from the local manifest.json file.
    """
    try:
        # Check if manifest.json file exists locally
        if not os.path.exists(LOCAL_MANIFEST_PATH):
            print("The manifest.json file is not found locally.")
            return None

        # Load the current version from the local manifest.json
        with open(LOCAL_MANIFEST_PATH, "r") as local_manifest_file:
            local_manifest = json.load(local_manifest_file)
            return local_manifest.get("version")

    except Exception as e:
        print(f"An error occurred while retrieving the version: {e}")
        return None


def get_project_info():
    """
    Get project information such as author and license from the local manifest.json file.
    """
    try:
        # Check if manifest.json file exists locally
        if not os.path.exists(LOCAL_MANIFEST_PATH):
            print("The manifest.json file is not found locally.")
            return None, None

        # Load project information from the local manifest.json
        with open(LOCAL_MANIFEST_PATH, "r") as local_manifest_file:
            local_manifest = json.load(local_manifest_file)
            author = local_manifest.get("author")
            license = local_manifest.get("license")
            return author, license

    except Exception as e:
        print(f"An error occurred while retrieving project information: {e}")
        return None, None


if __name__ == "__main__":
    current_version = get_current_version()
    author, license = get_project_info()
    if current_version:
        print(f"Current version: {current_version}")
    if author:
        print(f"Author: {author}")
    if license:
        print(f"License: {license}")
