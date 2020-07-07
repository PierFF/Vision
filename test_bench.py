import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtGui import QIcon
from testbench_UI import Ui_TestBench
from widgets.image_tab import ImageTab

import json
import os


class MainWindow(QMainWindow, Ui_TestBench):
    version = 0.1
    file_settings_name = "TestBench.prefs"
    current_dir = ""
    tabs = {}
    settings = {}

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_TestBench.__init__(self)
        self.setupUi(self)
        self.statusbar.showMessage(
            "TestBench v{} - INSA Toulouse".format(self.version)
            )
        self.tabsWidget.removeTab(0)

        # Load Preferences
        self.load_settings()

        # Set close action
        self.action_Quit.triggered.connect(self.close)
        self.action_Quit.setIcon(QIcon("./img/close.png"))

        # Set open action
        self.action_Open.triggered.connect(self.open)
        self.action_Open.setIcon(QIcon("./img/open.png"))

        # Set save action
        self.action_Save.triggered.connect(self.open)
        self.action_Save.setIcon(QIcon("./img/save.png"))

        # Specify cose action for tabsWidget

        self.tabsWidget.tabCloseRequested.connect(self.removeTab)

    def removeTab(self, tab_index):
        self.tabsWidget.removeTab(tab_index)

    def message(self, text):
        self.messagesWidget.appendPlainText(text)

    def load_settings(self):
        if os.path.exists(self.file_settings_name):
            f = open(self.file_settings_name, 'r')
            self.settings = json.load(f)
            f.close()
    
    def save_preferences(self):
        f = open(self.file_settings_name, 'w')
        json.dump(self.settings, f)
        f.close()

    def open(self):
        fd = QFileDialog(self)
        fd.setNameFilter("Tiff Images (*.tiff *.tif *.png)")
        fd.setFileMode(fd.ExistingFile)
        if self.settings is not None:
            last_dir = self.settings.get("last_dir", None)
            if last_dir is not None:
                fd.setDirectory(last_dir)
        else:
            self.settings = {}
        if fd.exec():
            f = fd.selectedFiles()[0]
            self.settings['last_dir'] = os.path.dirname(f)
            self.save_preferences()
        itab = ImageTab(self)
        itab.message.connect(self.message)
        self.tabsWidget.addTab(itab, os.path.basename(f))
        self.tabsWidget.setCurrentIndex(self.tabsWidget.indexOf(itab))
        itab.open(f)

    def save(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
