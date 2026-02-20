#!/bin/bash
set -e

echo "=== Warp Control Installer ==="

# Detect package manager
if command -v apt &> /dev/null; then
    echo "Installing PyQt5 via apt..."
    sudo apt update
    sudo apt install -y python3-pyqt5
elif command -v dnf &> /dev/null; then
    echo "Installing PyQt5 via dnf..."
    sudo dnf install -y python3-pyqt5
elif command -v pacman &> /dev/null; then
    echo "Installing PyQt5 via pacman..."
    sudo pacman -S --noconfirm python-pyqt5
elif command -v pip3 &> /dev/null; then
    echo "Installing PyQt5 via pip3..."
    pip3 install --user PyQt5
else
    echo "Error: No supported package manager found"
    exit 1
fi

# Install to /opt
echo "Installing application..."
sudo mkdir -p /opt/warp-control
sudo cp warp_gui.py /opt/warp-control/
sudo cp warp-icon.svg /opt/warp-control/
sudo chmod +x /opt/warp-control/warp_gui.py

# Create desktop file
cat > /tmp/warp-control.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Warp Control
Comment=Control Cloudflare Warp VPN
Exec=/opt/warp-control/warp_gui.py
Icon=/opt/warp-control/warp-icon.svg
Terminal=false
Categories=Network;Utility;
EOF

# Install desktop file
sudo cp /tmp/warp-control.desktop /usr/share/applications/
mkdir -p ~/.local/share/applications
cp /tmp/warp-control.desktop ~/.local/share/applications/

# Desktop shortcut
if [ -d ~/Desktop ]; then
    cp /tmp/warp-control.desktop ~/Desktop/
    chmod +x ~/Desktop/warp-control.desktop
fi

echo "✓ Installation complete!"
echo "Launch 'Warp Control' from your application menu"
