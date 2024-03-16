import os
import json
import platform
from distutils.version import LooseVersion
import requests

# Emojis
EMOJI_ROCKET = "🚀"
EMOJI_WARNING = "⚠️"

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Local manifest.json path
LOCAL_MANIFEST_PATH = os.path.join(current_dir,'..', 'manifest.json')


# Remote manifest.json URL
REMOTE_MANIFEST_URL = "https://raw.githubusercontent.com/orbitturner/directory-mapper/main/dirmap/manifest.json"


def check_for_update():
    print(f"{EMOJI_ROCKET} Checking for updates...")

    # Check if manifest.json file exists locally
    if not os.path.exists(LOCAL_MANIFEST_PATH):
        print(f"{EMOJI_WARNING} The manifest.json file is not found locally.")
        return

    try:
        # Load the current version from the local manifest.json
        with open(LOCAL_MANIFEST_PATH, "r") as local_manifest_file:
            local_manifest = json.load(local_manifest_file)
            local_version = local_manifest.get("version")

        if not local_version:
            print(f"{EMOJI_WARNING} Unable to retrieve the version from the local manifest.json.")
            return

        # Download the remote manifest.json
        remote_manifest_response = requests.get(REMOTE_MANIFEST_URL)
        remote_manifest = remote_manifest_response.json()
        remote_version = remote_manifest.get("version")

        if not remote_version:
            print(f"{EMOJI_WARNING} Unable to retrieve the version from the remote manifest.json.")
            return

        # Compare versions
        if LooseVersion(remote_version) > LooseVersion(local_version):
            print(f"{EMOJI_WARNING} New version available: {remote_version}")
            install_command = get_install_command()
            print(f"🔁 To update, execute the following command:\n{install_command}")
        else:
            print("No updates available.")
    except Exception as e:
        print(f"{EMOJI_WARNING} An error occurred while checking for updates: {e}")

def get_install_command():
    # Determine the operating system
    os_name = platform.system()

    if os_name == "Windows":
        return "pip install directory-mapper --force"
    elif os_name == "Linux":
        return "pip install directory-mapper --force"
    else:
        return f"The operating system {os_name} is not supported."

if __name__ == "__main__":
    check_for_update()
