import json
from wonderwords import RandomWord
from datetime import datetime
from subprocess import check_output, run

def get_version_type():
    print("🚀 Quel type de version voulez-vous déployer ?")
    print("1. Major")
    print("2. Minor")
    print("3. Patch")

    choice = input("Entrez le numéro correspondant : ")
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
    with open("manifest.json", "r+") as manifest_file:
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
    print("📡 Commiting files to Git")
    run(["git", "add", "."], check=True)
    run(["git", "commit", "-m", commit_message], check=True)
    print(f"🚀 Pushing to Git on branch {branch}")
    run(["git", "push", "origin", branch], check=True)
    print("✅ Push to Git successful")


def main():
    print("🌟 Début du déploiement 🌟")

     # Récupérer la version actuelle depuis le manifest.json
    with open("manifest.json") as manifest_file:
        manifest = json.load(manifest_file)
        current_version = manifest["version"]
        deploy_branch = manifest.get("deploy-branch", "main")  # Si la clé n'est pas spécifiée, utiliser "main"
        print(f"Version actuelle dans manifest.json : {current_version}")
        print(f"Branche de déploiement : {deploy_branch}")

    version_type = get_version_type()
    print(f"Type de version sélectionné : {version_type}")

    # Incrémenter la version
    new_version = increment_version(current_version, version_type)
    print(f"🔼 Nouvelle version générée : {new_version}")

    commit_message = get_last_commit_message()
    print(f"📝 Message du dernier commit : {commit_message}")

    # Mettre à jour la version dans manifest.json
    update_manifest_version(new_version)
    print("✅ Version mise à jour dans manifest.json")

    # Mettre à jour version-history.json
    update_version_history(new_version, commit_message)
    print("✅ Version ajoutée à version-history.json")

    # Push to Git
    push_to_git(deploy_branch, commit_message)

    print("🎉 Déploiement réussi ! 🎉")

if __name__ == "__main__":
    main()
