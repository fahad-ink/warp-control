#!/bin/bash
set -e

echo "=== Building Warp Control AppImage ==="

# Create AppDir structure
mkdir -p WarpControl.AppDir/usr/bin
mkdir -p WarpControl.AppDir/usr/share/applications
mkdir -p WarpControl.AppDir/usr/share/icons

# Copy files
cp warp_gui.py WarpControl.AppDir/usr/bin/warp-control
cp warp-icon.svg WarpControl.AppDir/usr/share/icons/warp-control.svg
cp warp-icon.svg WarpControl.AppDir/warp-control.svg

# Create desktop file
cat > WarpControl.AppDir/warp-control.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Warp Control
Comment=Control Cloudflare Warp VPN
Exec=warp-control
Icon=warp-control
Terminal=false
Categories=Network;Utility;
EOF

cp WarpControl.AppDir/warp-control.desktop WarpControl.AppDir/usr/share/applications/

# Create AppRun
cat > WarpControl.AppDir/AppRun << 'EOF'
#!/bin/bash
APPDIR="$(dirname "$(readlink -f "$0")")"
exec python3 "$APPDIR/usr/bin/warp-control" "$@"
EOF
chmod +x WarpControl.AppDir/AppRun

# Download appimagetool if not exists
if [ ! -f appimagetool-x86_64.AppImage ]; then
    wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
    chmod +x appimagetool-x86_64.AppImage
fi

# Build AppImage
./appimagetool-x86_64.AppImage WarpControl.AppDir warp-control-x86_64.AppImage

echo "✓ AppImage created: warp-control-x86_64.AppImage"
