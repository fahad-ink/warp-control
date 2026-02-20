#!/usr/bin/env python3
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGroupBox, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QFont, QIcon

class CommandThread(QThread):
    finished = pyqtSignal(str)
    
    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd
    
    def run(self):
        try:
            result = subprocess.run(self.cmd, shell=True, capture_output=True, text=True, timeout=10)
            output = result.stdout.strip() or result.stderr.strip() or "✓ Done"
            self.finished.emit(output)
        except Exception as e:
            self.finished.emit(f"✗ Error: {e}")

class WarpGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warp Control")
        self.setFixedSize(450, 550)
        self.setStyleSheet("""
            QMainWindow { background: #1e1e2e; }
            QGroupBox { 
                color: #cdd6f4; 
                font-size: 14px; 
                font-weight: bold; 
                border: 2px solid #45475a;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; }
            QPushButton {
                background: #89b4fa;
                color: #1e1e2e;
                border: none;
                border-radius: 6px;
                padding: 14px;
                font-size: 14px;
                font-weight: bold;
                min-height: 20px;
            }
            QPushButton:hover { background: #b4befe; }
            QPushButton:pressed { background: #74c7ec; }
            QPushButton:disabled { background: #45475a; color: #6c7086; }
            QLabel {
                background: #313244;
                color: #cdd6f4;
                border-radius: 6px;
                padding: 12px;
                font-size: 12px;
            }
        """)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Status Label at top
        self.status_label = QLabel("Checking status...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            QLabel {
                background: #313244;
                color: #a6e3a1;
                border-radius: 6px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.status_label)
        
        # Connection Group
        conn_group = QGroupBox("Connection")
        conn_layout = QVBoxLayout()
        conn_layout.setSpacing(8)
        
        self.add_button(conn_layout, "📝 Register", "warp-cli register")
        
        self.connect_btn = QPushButton("🔌 Connect")
        self.connect_btn.clicked.connect(lambda: self.run_cmd("warp-cli connect"))
        conn_layout.addWidget(self.connect_btn)
        
        self.disconnect_btn = QPushButton("🔌 Disconnect")
        self.disconnect_btn.clicked.connect(lambda: self.run_cmd("warp-cli disconnect"))
        conn_layout.addWidget(self.disconnect_btn)
        
        self.add_button(conn_layout, "📊 Status", "warp-cli status")
        
        conn_group.setLayout(conn_layout)
        layout.addWidget(conn_group)
        
        # Service Group
        svc_group = QGroupBox("Service Management")
        svc_layout = QVBoxLayout()
        svc_layout.setSpacing(8)
        
        self.add_button(svc_layout, "⏹️ Stop Service", "pkexec systemctl stop warp-svc")
        self.add_button(svc_layout, "❌ Disable Service", "pkexec systemctl disable warp-svc")
        self.add_button(svc_layout, "✅ Enable Service", "pkexec systemctl enable warp-svc")
        self.add_button(svc_layout, "▶️ Start Service", "pkexec systemctl start warp-svc")
        
        svc_group.setLayout(svc_layout)
        layout.addWidget(svc_group)
        
        # Command output
        self.output = QLabel("Ready")
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setWordWrap(True)
        self.output.setMinimumHeight(60)
        layout.addWidget(self.output)
        
        # System tray
        self.tray = QSystemTrayIcon(QIcon("/opt/warp-control/warp-icon.svg"), self)
        tray_menu = QMenu()
        show_action = QAction("Show", self)
        show_action.triggered.connect(self.show)
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(QApplication.quit)
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray.setContextMenu(tray_menu)
        self.tray.activated.connect(self.tray_clicked)
        self.tray.show()
        
        # Auto-update status
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_status)
        self.timer.start(2000)
        self.check_status()
    
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray.showMessage("Warp Control", "Minimized to tray", QSystemTrayIcon.Information, 2000)
    
    def tray_clicked(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()
                self.activateWindow()
                self.raise_()
    
    def check_status(self):
        try:
            result = subprocess.run("warp-cli status", shell=True, capture_output=True, text=True, timeout=5)
            output = result.stdout.strip()
            if "Connected" in output:
                self.status_label.setText("🟢 Connected")
                self.status_label.setStyleSheet("QLabel { background: #313244; color: #a6e3a1; border-radius: 6px; padding: 12px; font-size: 14px; font-weight: bold; }")
                self.connect_btn.setEnabled(False)
                self.disconnect_btn.setEnabled(True)
            else:
                self.status_label.setText("🔴 Disconnected")
                self.status_label.setStyleSheet("QLabel { background: #313244; color: #f38ba8; border-radius: 6px; padding: 12px; font-size: 14px; font-weight: bold; }")
                self.connect_btn.setEnabled(True)
                self.disconnect_btn.setEnabled(False)
        except:
            self.status_label.setText("⚠️ Status Unknown")
    
    def add_button(self, layout, text, cmd):
        btn = QPushButton(text)
        btn.clicked.connect(lambda: self.run_cmd(cmd))
        layout.addWidget(btn)
    
    def run_cmd(self, cmd):
        self.output.setText("⏳ Running...")
        self.thread = CommandThread(cmd)
        self.thread.finished.connect(self.on_cmd_finished)
        self.thread.start()
    
    def on_cmd_finished(self, result):
        self.output.setText(result)
        self.check_status()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarpGUI()
    window.show()
    sys.exit(app.exec_())
