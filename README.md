Orbit Directory Mapper 🌌
=========================

Bienvenue dans Orbit Directory Mapper, votre outil de visualisation et de création d'arborescences de répertoires.

Fonctionnalités 💡
------------------

*   Visualisation en ASCII, JSON ou YAML de la structure d'un dossier.
*   Création d'arborescences à partir de descriptions JSON.
*   Export & Compression de la structure d'un dossier au format JSON ou YAML.

Prérequis 🛠
------------

*   **Python** installé sur votre machine.
*   **Git** installé sur votre machine.

Installation 📥
---------------

### Installation sur Windows
```powershell
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/orbitturner/directory-mapper/main/setups/install.ps1')
```
### Installation sur Linux
```shell
wget -O - https://raw.githubusercontent.com/orbitturner/directory-mapper/main/setups/install.sh | bash
```


Démarrage 🚀
------------

Après l'installation, vous pouvez utiliser l'alias `dirmap` sur la ligne de commande.

Utilisation 🧑‍💻
-----------------

Vous pouvez utiliser le script pour visualiser la structure d'un dossier ou créer une arborescence à partir d'une description JSON.

Utilisez l'outil Orbit Directory Mapper pour explorer la structure d'un dossier ou créer une arborescence.

### Afficher la Structure d'un Dossier
```shell
dirmap chemin/du/dossier --ignore dossier1 dossier2 --regex "^test.*$"
```
*   `chemin/du/dossier` : Chemin du dossier à explorer.
*   `--ignore dossier1 dossier2` : Noms des dossiers à ignorer.
*   `--regex "^test.*$"` : Motif regex pour ignorer certains dossiers.
*   `--format "json" or "yaml` _(optional)_: Format d'affichage de l'arborescence (JSON ou YAML). If Not set ASCII will be used.

### Créer une Arborescence à partir d'une Description JSON
```shell
dirmap chemin/du/dossier --create --description chemin/vers/description.json --ignore dossier1 dossier2 --format json
```
*   `chemin/du/dossier` : Chemin du dossier à créer.
*   `--create` : Mode création d'arborescence.
*   `--description chemin/vers/description.json` : Chemin de la description JSON pour le mode création.
*   `--ignore dossier1 dossier2` : Noms des dossiers à ignorer.




Documentation 📖
----------------

Consultez la documentation complète sur l'utilisation de l'outil dans le fichier `docs/README.md`.

Contribuer 🌟
-------------

Si vous souhaitez contribuer à ce projet, consultez le guide de contribution dans le fichier `CONTRIBUTING.md`.

Licence 📜
----------

Ce projet est sous licence MIT. Consultez le fichier `LICENCE` pour plus d'informations.

Contact 📞
----------

Pour toute question ou préoccupation, n'hésitez pas à me contacter à .