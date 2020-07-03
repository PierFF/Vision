import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtGui import QIcon
from testbench_UI import Ui_TestBench
from image_tab import ImageTab

import json
import os


class MainWindow(QMainWindow, Ui_TestBench):
    version = 0.1
    file_prefs_name = "TestBench.prefs"
    current_dir = ""
    tabs = {}

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_TestBench.__init__(self)
        self.setupUi(self)
        self.statusbar.showMessage(
            "TestBench v{} - INSA Toulouse".format(self.version)
            )
        self.tabsWidget.removeTab(0)

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

    def load_preferences(self):
        if os.path.exists(self.file_prefs_name):
            f = open(self.file_prefs_name, 'r')
            prefs = json.load(f)
            f.close()
            return prefs
        else:
            return None

    def save_preferences(self, prefs):
        f = open(self.file_prefs_name, 'w')
        json.dump(prefs, f)
        f.close()

    def open(self):
        fd = QFileDialog(self)
        fd.setNameFilter("Tiff Images (*.tiff *.tif *.png)")
        fd.setFileMode(fd.ExistingFile)
        prefs = self.load_preferences()
        if prefs is not None:
            last_dir = prefs.get("last_dir", None)
            if last_dir is not None:
                fd.setDirectory(last_dir)
        else:
            prefs = {}
        if fd.exec():
            f = fd.selectedFiles()[0]
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
