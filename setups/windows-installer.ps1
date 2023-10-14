# windows-installer.ps1

Write-Host "🚀 Installation Start 🚀"

# Test administrative privileges
$adminRights = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# Check if the user has administrator rights
if (-not $adminRights) {
    return Write-Host "❌ Please, run this script as an administrator. Right-click the PowerShell icon and select 'Run as Administrator.' 😫😫 Are you Mad ?!"
}

$installPath = "C:\Program Files\OrbitDirectoryMapper"

# Check if a previous installation exists
if (Test-Path $installPath) {
    $reinstall = $null
    while ($reinstall -ne 'Y' -and $reinstall -ne 'N') {
        $reinstall = Read-Host "Program is already installed at $installPath. Do you want to reinstall? (Y/N)"
    }

    if ($reinstall -eq 'Y') {
        # Remove the existing program and its entry from the environment
        Write-Host "🗑 Uninstalling existing program..."
        Remove-Item -Recurse -Force $installPath

        # Remove entry from the environment
        $envPath = [System.Environment]::GetEnvironmentVariable('Path', [System.EnvironmentVariableTarget]::Machine)
        $newPath = $envPath -replace [regex]::Escape("$installPath;"), ''
        [System.Environment]::SetEnvironmentVariable('Path', $newPath, [System.EnvironmentVariableTarget]::Machine)
    } else {
        return Write-Host "🚫 Installation aborted by user."
    }
}
Write-Host "🛠 Checking installation of Python and Git"

# Check if Python is installed
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed. Please install Python before continuing." -ForegroundColor Red
    exit 1
}

# Check if Git is installed
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git is not installed. Please install Git before continuing." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Python and Git are installed."

Write-Host "📦 Installing Python dependencies"

# Install Python dependencies
python -m pip install loguru
python -m pip install pyyaml
python -m pip install termcolor
python -m pip install art
python -m pip install wonderwords
python -m pip install requests
python -m pip install rich

Write-Host "✅ Python dependencies installed."

Write-Host "📥 Cloning the repository from GitHub"

# Clone the repository from GitHub
git clone https://github.com/orbitturner/directory-mapper $installPath

# Create a batch script to run the application
Write-Host "📝 Creating the application execution script"
Add-Content "$installPath\dirmap.bat" "@echo off"
Add-Content "$installPath\dirmap.bat" "python `"$installPath\orbit_directory_mapper.py`" `%`*"

# Add the applications directory to the PATH
$newPath = [System.Environment]::GetEnvironmentVariable('Path', [System.EnvironmentVariableTarget]::Machine) + ";$installPath"
[Environment]::SetEnvironmentVariable("Path", $newPath, [EnvironmentVariableTarget]::Machine)

# Execute the refreshenv command to reflect changes in the environment
Write-Host "🔄 Refreshing the environment..."
refreshenv

Write-Host "✅ Repository cloned and alias added to the environment."

Write-Host "🎉 Successful installation in $installPath. "

Write-Host "🚀 You can now use the 'dirmap' command from your terminal 🚀"

dirmap --help
