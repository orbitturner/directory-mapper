import json
import sys
import os
from wonderwords import RandomWord
from datetime import datetime
from subprocess import check_output, run, CalledProcessError
from loguru import logger
import shutil

MANIFEST_FILE = "dirmap/manifest.json"

def get_version_type():
    print("🚀 What type of version do you want to deploy?")
    print("1. Major")
    print("2. Minor")
    print("3. Patch")

    choice = input("Enter the corresponding number: ")
    return {"1": "major", "2": "minor", "3": "patch"}.get(choice)

def increment_version(version, version_type):
    major, minor, patch = map(int, version.split('.'))
    if version_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif version_type == "minor":
        minor += 1
        patch = 0
    elif version_type == "patch":
        patch += 1

    return f"{major}.{minor}.{patch}"

def generate_version_name():
    r = RandomWord()
    return f"{r.word()}-{r.word(include_parts_of_speech=['adjectives'])}"

def get_last_commit_message():
    return check_output(["git", "log", "-1", "--pretty=%B"]).decode().strip()

def update_manifest_version(version):
    with open(MANIFEST_FILE, "r+") as manifest_file:
        manifest = json.load(manifest_file)
        manifest["version"] = version
        manifest_file.seek(0)
        json.dump(manifest, manifest_file, indent=4)
        manifest_file.truncate()

def update_version_history(version, commit_message):
    entry = {
        "version": version,
        "date": datetime.today().strftime('%Y-%m-%d'),
        "description": commit_message,
        "name": generate_version_name()
    }

    with open("versions-history.json", "r+") as version_history_file:
        data = json.load(version_history_file)
        data.append(entry)
        version_history_file.seek(0)
        json.dump(data, version_history_file, indent=4)
        version_history_file.truncate()

def push_to_git(branch, commit_message):
    logger.info("📡 Committing files to Git")
    run(["git", "add", "."], check=True)
    run(["git", "commit", "-m", commit_message], check=True)
    logger.info(f"🚀 Pushing to Git on branch {branch}")
    try:
        run(["git", "push", "origin", branch], check=True)
    except CalledProcessError as e:
        logger.error(f"❌ Error pushing to Git: {e}")
        sys.exit(1)
    logger.info("✅ Push to Git successful")
    
    # Execute additional operations after push
    execute_additional_operations()

def execute_additional_operations():
    logger.info("🔧 Executing additional operations after push")
    try:
        # Execute `python setup.py sdist bdist_wheel`
        logger.info("📦 Building distribution packages")
        run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)

        # Execute `twine upload dist/*`
        logger.info("🚀 Uploading distribution packages to PyPI")
        run(["twine", "upload", "dist/*"], check=True)

        # Remove directories: 'directory_mapper.egg-info', 'build', and 'dist'
        logger.info("🗑 Cleaning up build artifacts")
        directories_to_remove = ['directory_mapper.egg-info', 'build', 'dist']
        for directory in directories_to_remove:
            shutil.rmtree(directory, ignore_errors=True)

        logger.info("✅ Clean up successful")
    except CalledProcessError as e:
        logger.error(f"❌ Error executing additional operations: {e}")
        sys.exit(1)

def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logFileName = os.path.join(current_dir, "dirmap_logs", "dirmap_events.log")
    # Configure logs with Loguru
    logger.remove()
    logger.add(logFileName, rotation="10 MB", level="DEBUG")
    # Add another handler for the console, but only for INFO and higher levels
    logger.add(sys.stdout, level="INFO")

    logger.info("🌟 Deployment Start 🌟")

    # Get the current version from manifest.json
    with open(MANIFEST_FILE) as manifest_file:
        manifest = json.load(manifest_file)
        current_version = manifest["version"]
        deploy_branch = manifest.get("deploy-branch", "main")  # If the key is not specified, use "main"
        logger.info(f"Current version in manifest.json: {current_version}")
        logger.info(f"Deployment branch: {deploy_branch}")

    version_type = get_version_type()
    logger.info(f"Selected version type: {version_type}")

    # Increment the version
    new_version = increment_version(current_version, version_type)
    logger.info(f"🔼 New version generated: {new_version}")

    commit_message = get_last_commit_message()
    logger.info(f"📝 Last commit message: {commit_message}")

    # Update the version in manifest.json
    update_manifest_version(new_version)
    logger.info("✅ Version updated in manifest.json")

    # Update version-history.json
    update_version_history(new_version, commit_message)
    logger.info("✅ Version added to version-history.json")

    # Push to Git
    push_to_git(deploy_branch, commit_message)

    logger.info("🎉 Deployment successful! 🎉")

if __name__ == "__main__":
    main()
