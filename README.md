<div align="center">

# 🚀 Warp Control

### Modern GUI for Cloudflare Warp VPN on Linux

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.0+-green.svg)](https://pypi.org/project/PyQt5/)
[![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)](https://www.linux.org/)

![Warp Control](https://raw.githubusercontent.com/fahad-ink/warp-control/main/warp-icon.svg)

*A beautiful, feature-rich desktop application to control Cloudflare Warp VPN with ease*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots)

</div>

---

## ✨ Features

- 🎨 **Modern Dark Theme** - Beautiful Catppuccin-inspired interface
- 🔌 **Quick Controls** - Connect/Disconnect with a single click
- 📊 **Real-time Status** - Live connection status monitoring
- ⚙️ **Service Management** - Full control over Warp service
- 📝 **Easy Registration** - Register your device directly from GUI
- 🔔 **System Tray** - Minimize to tray and quick access
- 🚀 **Auto-refresh** - Status updates every 2 seconds
- 💡 **Smart UI** - Buttons auto-disable based on connection state

## 📦 Installation

### Quick Install (Debian/Ubuntu)

```bash
wget https://github.com/fahad-ink/warp-control/releases/download/v1.0/warp-control_1.0.deb
sudo dpkg -i warp-control_1.0.deb
```

### Universal Install (All Linux Distros)

```bash
git clone https://github.com/fahad-ink/warp-control.git
cd warp-control
chmod +x install.sh
./install.sh
```

**Supported Package Managers:**
- 📦 APT (Debian/Ubuntu)
- 📦 DNF (Fedora/RHEL)
- 📦 Pacman (Arch)
- 📦 pip3 (Fallback)

## 🚀 Usage

### Launch from Application Menu
Search for **"Warp Control"** in your application launcher

### Or run from terminal
```bash
/opt/warp-control/warp_gui.py
```

### First Time Setup
1. Click **"📝 Register"** to register your device
2. Click **"🔌 Connect"** to start VPN
3. Minimize to system tray when not needed

## 🎯 Requirements

- Python 3.6+
- PyQt5
- Cloudflare Warp CLI (`warp-cli`)

### Install Cloudflare Warp

**Debian/Ubuntu:**
```bash
curl -fsSL https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/cloudflare-client.list
sudo apt update && sudo apt install cloudflare-warp
```

## 🎨 Screenshots

> *Coming soon - Add your screenshots here*

## 🗑️ Uninstall

### Debian/Ubuntu (.deb)
```bash
sudo apt remove warp-control
```

### Manual Installation
```bash
cd warp-control
chmod +x uninstall.sh
./uninstall.sh
```

## 🛠️ Controls Explained

### Connection Controls
- **📝 Register** - Register device with Cloudflare (one-time)
- **🔌 Connect** - Connect to Warp VPN
- **🔌 Disconnect** - Disconnect from VPN
- **📊 Status** - Check current connection status

### Service Management
- **▶️ Start Service** - Start Warp background service
- **⏹️ Stop Service** - Stop Warp service temporarily
- **✅ Enable Service** - Auto-start on boot
- **❌ Disable Service** - Prevent auto-start on boot

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📄 License

MIT License - feel free to use this project however you'd like!

## 🙏 Acknowledgments

- Built with [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- Powered by [Cloudflare Warp](https://1.1.1.1/)
- Inspired by modern Linux desktop applications

---

<div align="center">

Made with ❤️ for the Linux community

⭐ Star this repo if you find it useful!

</div>
