#!/bin/bash

echo "🚀 Désinstallation en cours 🚀"

# Vérifier les privilèges administratifs
if [ "$EUID" -ne 0 ]; then
    echo "❌ Veuillez exécuter ce script en tant qu'administrateur (utilisez sudo)." >&2
    exit 1
fi

installPath="/usr/local/OrbitDirectoryMapper"
binApp="/usr/local/bin/dirmap"

# Vérifier si une installation précédente existe
if [ -d "$installPath" ]; then
    read -p "Le programme est déjà installé à $installPath. Voulez-vous le desinstaller ? (O/N) : " reinstall

    if [ "$reinstall" == "O" ]; then
        # Désinstaller le programme existant et supprimer son entrée de l'environnement
        echo "🗑 Désinstallation du programme existant..."
        rm -rf "$installPath"
        rm -rf "$binApp"

        # Supprimer l'entrée de l'environnement
        export PATH=$(echo $PATH | sed -e "s|$installPath;||")
    else
        echo "🚫 Désinstallation annulée par l'utilisateur."
        exit 1
    fi
fi

echo "✅ Désinstallation terminée."
