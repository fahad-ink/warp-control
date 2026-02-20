# Warp Control

Modern GUI for Cloudflare Warp VPN on Linux

## Features
- 🎨 Modern dark theme interface
- 🔌 Connect/Disconnect controls
- 📊 Real-time connection status
- ⚙️ Service management
- 📝 Device registration
- 🔔 System tray integration

## Installation

```bash
chmod +x install.sh
./install.sh
```

Supports: Debian/Ubuntu (apt), Fedora/RHEL (dnf), Arch (pacman)

## Usage

Launch from application menu or run:
```bash
/opt/warp-control/warp_gui.py
```

## Uninstall

```bash
chmod +x uninstall.sh
./uninstall.sh
```

## Requirements
- Python 3
- PyQt5
- warp-cli (Cloudflare Warp)
