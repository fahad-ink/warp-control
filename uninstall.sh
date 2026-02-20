#!/bin/bash
set -e

echo "=== Warp Control Uninstaller ==="

sudo rm -rf /opt/warp-control
sudo rm -f /usr/share/applications/warp-control.desktop
rm -f ~/.local/share/applications/warp-control.desktop
rm -f ~/Desktop/warp-control.desktop

echo "✓ Uninstallation complete!"
