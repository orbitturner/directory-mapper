#!/bin/bash

echo "🚀 Installation Start 🚀"

# Check for administrative privileges
if [ "$EUID" -ne 0 ]; then
    echo "❌ Please run this script as an administrator (use sudo)." >&2
    exit 1
fi

installPath="/usr/local/OrbitDirectoryMapper"

# Check if a previous installation exists
if [ -d "$installPath" ]; then
    read -p "The program is already installed at $installPath. Do you want to reinstall? (Y/N): " reinstall

    if [ "$reinstall" == "Y" ]; then
        # Uninstall the existing program and remove its entry from the environment
        echo "🗑 Uninstalling the existing program..."
        rm -rf "$installPath"

        # Remove entry from the environment
        export PATH=$(echo $PATH | sed -e "s|$installPath;||")
    else
        echo "🚫 Installation aborted by the user."
        exit 1
    fi
fi

echo "🛠 Checking installation of Python and Git"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python before continuing." >&2
    exit 1
fi

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git before continuing." >&2
    exit 1
fi

echo "✅ Python and Git are installed."

echo "📦 Installing Python dependencies"

# Install Python dependencies
pip install loguru
pip install pyyaml
pip install termcolor
pip install art
pip install wonderwords
pip install requests
pip install rich


echo "✅ Python dependencies installed."

echo "📥 Cloning the repository from GitHub"

# Clone the repository from GitHub
git clone https://github.com/orbitturner/directory-mapper "$installPath"

# Create a script to run the application
echo "📝 Creating the application execution script"
echo -e "#!/bin/bash\npython \"$installPath/orbit_directory_mapper.py\" \"$@\"" > "$installPath/dirmap"
chmod +x "$installPath/dirmap"

# Add the applications directory to the PATH
export PATH=$PATH:$installPath

echo "✅ Repository cloned and alias added to the environment."

echo "🎉 Successful installation in $installPath."

echo "🚀 You can now use the dirmap command from your terminal 🚀"

dirmap --help