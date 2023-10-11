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
    Write-Host "❌ Une ancienne installation existe déjà. Veuillez désinstaller avant de continuer."
    exit 1
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

Write-Host "✅ Dépendances Python installées."

Write-Host "📥 Clonage du repository depuis GitHub"

# Cloner le repository depuis GitHub
git clone https://github.com/orbitturner/directory-mapper $installPath

# Ajouter l'alias dans l'environnement
$env:Path = $env:Path + ";" + $installPath
[Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)

# Ajouter l'alias dirmap
$env:Path = $env:Path + ";" + $installPath
[Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)
[Environment]::SetEnvironmentVariable("dirmap", "$installPath\orbit_directory_mapper.py", [System.EnvironmentVariableTarget]::Machine)

Write-Host "✅ Repository cloné et alias ajouté à l'environnement."

Write-Host "🎉 Installation réussie dans $installPath. L'alias dirmap a été ajouté à l'environnement."
