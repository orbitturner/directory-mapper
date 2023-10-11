#!/bin/bash

echo "🚀 Début de l'installation 🚀"

# Vérifie si le script est exécuté en tant que root (administrateur)
if [ "$EUID" -ne 0 ]; then
    echo "❌ Please run this script as root (administrator). Use 'sudo ./linux-installer.sh'. 😫 Are you Mad ?!"
    exit 1
fi

installPath="/usr/local/bin/OrbitDirectoryMapper"

# Vérifier si une ancienne installation existe
if [ -d "$installPath" ]; then
    echo "❌ Une ancienne installation existe déjà. Veuillez désinstaller avant de continuer."
    exit 1
fi

echo "🛠 Vérification de l'installation de Python et Git"

# Vérifier si Python est installé
if ! command -v python &> /dev/null; then
    echo "❌ Python n'est pas installé. Veuillez installer Python avant de continuer."
    exit 1
fi

# Vérifier si Git est installé
if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé. Veuillez installer Git avant de continuer."
    exit 1
fi

echo "✅ Python et Git sont installés."

echo "📦 Installation des dépendances Python"

# Installer les dépendances Python
pip install loguru
pip install pyyaml
pip install termcolor
pip install art
pip install wonderwords


echo "✅ Dépendances Python installées."

echo "📥 Clonage du repository depuis GitHub"

# Cloner le repository depuis GitHub
git clone https://github.com/orbitturner/directory-mapper $installPath

echo "✅ Repository cloné."

echo "📝 Ajout des alias dans l'environnement"

# Ajouter l'alias dirmap
echo "export PATH=\$PATH:$installPath" >> ~/.bashrc
echo "alias dirmap=\"$installPath/orbit_directory_mapper.py\"" >> ~/.bashrc

source ~/.bashrc

echo "✅ Alias ajouté à l'environnement."

echo "🎉 Installation réussie dans $installPath. L'alias dirmap a été ajouté à l'environnement."
