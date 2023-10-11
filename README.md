🚀 **Orbit Directory Mapper**
=========================

💡 Unlock the power of directory management with Orbit Directory Mapper! View your file structures in ASCII, JSON, or YAML formats. 🌐 Effortlessly create directory trees using descriptive JSON files. Elevate your file organization game with ease. 🚀🌳 

📜 **Table of Contents**
---------------------

*   [Features](#features)
*   [Prerequisites](#prerequisites)
*   [Installation](#installation)
    *   [On Windows](#on-windows)
    *   [On Linux](#on-linux)
*   [Usage](#usage)
    *   [View Command (Default)](#view-command-default)
    *   [Create Command](#create-command)
    *   [Check-Update Command](#check-update-command)
*   [Updates](#updates)
*   [Contributions](#contributions)
*   [License](#license)
---------------------

🚀 **Features**
-----------

*   Visualization in ASCII, JSON, or YAML of a folder's structure.
*   Creation of tree structures from JSON descriptions.
*   Coming soon: Export & Compression of a folder's structure in JSON or YAML format.
*   Installation in one command.
*   Lightning-fast.
*   Easy to customize.


🛠 **Prerequisites**
------------

*   **Python** installed on your machine.
*   **Git** installed on your machine.


📥 **Installation**
---------------

### 🚀 **Installation on Windows**
```powershell	
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/orbitturner/directory-mapper/main/setups/windows-installer.ps1')
```

### 🐧 **Installation on Linux**
```bash
wget -O - https://raw.githubusercontent.com/orbitturner/directory-mapper/main/setups/linux-installer.ps1 | bash
```
  

🧑‍💻 **Usage**
-----------------

### View Command (Default)

This command is used to visualize the directory structure in ASCII art.

```shell
dirmap view \[--ignore <folder1 folder2>\] \[--regex <regex\_pattern>\] \[--format <json/yaml>\] <folder\_path>
```

*   `folder_path`: Path of the directory to explore.
*   `--ignore` _(optional)_: Specify folders to ignore.
*   `--regex` _(optional)_: Use a regex pattern to ignore certain folders.
*   `--format` _(optional)_: Display the directory structure in JSON or YAML format.

### Create Command

Use this command to create a directory structure based on a description file.

```shell
dirmap create --description <description\_file.json> \[--ignore <folder1 folder2>\] \[--regex <regex\_pattern>\] <folder\_path>
```

*   `folder_path`: Path of the directory where the structure will be created.
*   `--description`: Path of the JSON description file for the directory structure.
*   `--ignore` _(optional)_: Specify folders to ignore.
*   `--regex` _(optional)_: Use a regex pattern to ignore certain folders.

### Check-Update Command

This command checks for updates from the remote repository and provides instructions for the update.

```shell
dirmap check-update
```


  

🔄 **Updates**
---------------

Follow the [project's updates](./versions-history.json).

🤝 **Contributions**
----------------

Contributions are welcome! Check the [contribution guide](CONTRIBUTING.md) to get started.

📄 **License**
----------

This project is under the MIT license. Check the [LICENSE](LICENSE) file for more details.