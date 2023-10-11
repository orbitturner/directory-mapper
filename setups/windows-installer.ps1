# install.ps1

Write-Host "🚀 Début de l'installation 🚀"

# Teste les privilèges administratifs
$adminRights = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# Vérifie si l'utilisateur a les droits d'administrateur
if (-not $adminRights) {
    return Write-Host "❌ Please Bro RUN this script as an SUDO. Right-click the PowerShell icon and select 'Run as Administrator.' 😫😫 Are you Mad ?!"
}

$installPath = "C:\Program Files\OrbitDirectoryMapper"

# Vérifier si une ancienne installation existe
if (Test-Path $installPath) {
    $reinstall = $null
    while ($reinstall -ne 'Y' -and $reinstall -ne 'N') {
        $reinstall = Read-Host "Program is already installed at $installPath. Do you want to reinstall? (Y/N)"
    }

    if ($reinstall -eq 'Y') {
        # Supprimer le programme existant et son entrée dans l'environnement
        Write-Host "🗑 Uninstalling existing program..."
        Remove-Item -Recurse -Force $installPath

        # Supprimer l'entrée dans l'environnement
        $envPath = [System.Environment]::GetEnvironmentVariable('Path', [System.EnvironmentVariableTarget]::Machine)
        $newPath = $envPath -replace [regex]::Escape("$installPath;"), ''
        [System.Environment]::SetEnvironmentVariable('Path', $newPath, [System.EnvironmentVariableTarget]::Machine)
    } else {
        return Write-Host "🚫 Installation aborted by user."
    }
}
Write-Host "🛠 Vérification de l'installation de Python et Git"

# Vérifier si Python est installé
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python n'est pas installé. Veuillez installer Python avant de continuer." -ForegroundColor Red
    exit 1
}

# Vérifier si Git est installé
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git n'est pas installé. Veuillez installer Git avant de continuer." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Python et Git sont installés."

Write-Host "📦 Installation des dépendances Python"

# Installer les dépendances Python
pip install loguru
pip install pyyaml
pip install termcolor
pip install art
pip install wonderwords

Write-Host "✅ Dépendances Python installées."

Write-Host "📥 Clonage du repository depuis GitHub"

# Cloner le repository depuis GitHub
git clone https://github.com/orbitturner/directory-mapper $installPath

# Crée un script batch pour exécuter l'application
Write-Host "📝 Création du script d'exécution de l'application"
Add-Content "$installPath\dirmap.bat" "@echo off"
Add-Content "$installPath\dirmap.bat" "python `"$installPath\orbit_directory_mapper.py`" %*"

# Ajoute le répertoire des applications au PATH
$newPath = [System.Environment]::GetEnvironmentVariable('Path', [System.EnvironmentVariableTarget]::Machine) + ";$installPath"
[Environment]::SetEnvironmentVariable("Path", $newPath, [EnvironmentVariableTarget]::Machine)

# Exécute la commande refreshenv pour prendre en compte les changements dans l'environnement
Write-Host "🔄 Refreshing the environment..."
refreshenv

Write-Host "✅ Repository cloné et alias ajouté à l'environnement."

Write-Host "🎉 Installation réussie dans $installPath. "

Write-Host "🚀 Vous pouvez maintenant utiliser la commande dirmap depuis votre terminal 🚀"

