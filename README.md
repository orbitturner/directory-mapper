# 🚀 **Orbit Directory Mapper**

💡 Unlock the power of directory management with Orbit Directory Mapper! View your file structures in ASCII, JSON, or YAML formats. 🌐 Effortlessly create directory trees using descriptive JSON files. Elevate your file organization game with ease. 🚀🌳

<p align="center"> 
  <img src="https://github.com/orbitturner/directory-mapper/blob/5473bfd0d5d6e9a5ee66ac0126a18126512c66a1/.assets/dirmap_cover.png?raw=true" />
</p>

## 📜 **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [On Windows](#on-windows)
  - [On Linux](#on-linux)
- [Usage](#usage)
  - [View Command (Default)](#view-command-default)
  - [Create Command](#create-command)
  - [Check-Update Command](#check-update-command)
- [Updates](#updates)
- [Contributions](#contributions)
- [License](#license)

---

## 🚀 **Features**

- Visualization in ASCII, JSON, or YAML of a folder's structure.
- Creation of tree structures from JSON descriptions.
- Coming soon: Export & Compression of a folder's structure in JSON or YAML format.
- Installation in one command.
- Lightning-fast.
- Easy to customize.

## 🛠 **Prerequisites**

- **Python** installed on your machine.
- **Pip** installed on your machine.

## 📥 **Installation**

### 🚀 **Installation on Windows**

- Execute this command as Admin:

```bash
pip install directory-mapper --force

```

> **Note:** For updates, simply run the same command again.

### 🐧 **Installation on Linux**

```bash
pip install directory-mapper --force

```

For updates, simply run the same command again.

## 🧑‍💻 **Usage**

### View Command (Default)

This command is used to visualize the directory structure in ASCII art.

```shell
dirmap view \[--ignore <folder1 folder2>\] \[--regex <regex\_pattern>\] \[--format <json/yaml>\] <folder\_path>
```

- `folder_path`: Path of the directory to explore.
- `--ignore` _(optional)_: Specify folders to ignore.
- `--regex` _(optional)_: Use a regex pattern to ignore certain folders.
- `--format` _(optional)_: Display the directory structure in JSON or YAML format.

### Create Command

Use this command to create a directory structure based on a description file.

```shell
dirmap create --description <description\_file.json> \[--ignore <folder1 folder2>\] \[--regex <regex\_pattern>\] <folder\_path>
```

- `folder_path`: Path of the directory where the structure will be created.
- `--description`: Path of the JSON description file for the directory structure.
- `--ignore` _(optional)_: Specify folders to ignore.
- `--regex` _(optional)_: Use a regex pattern to ignore certain folders.

### Check-Update Command

This command checks for updates from the remote repository and provides instructions for the update.

```shell
dirmap check-update
```

## 🖼️ **Screenshots**

See the [Assets Folder](https://github.com/orbitturner/directory-mapper/tree/main/.assets) for more screens.

## 🔄 **Updates**

Follow the [project's updates](https://github.com/orbitturner/directory-mapper/blob/main/versions-history.json).

## 🤝 **Contributions**

Contributions are welcome! Check the [contribution guide](https://github.com/orbitturner/directory-mapper/blob/main/CONTRIBUTING.md) to get started.

## 📄 **License**

This project is under the MIT license. Check the [LICENSE](https://github.com/orbitturner/directory-mapper/blob/main/LICENSE.md) file for more details.
