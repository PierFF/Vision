import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication,\
     QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
from testbench_UI import Ui_TestBench
import json
import os


class MyWindow(QMainWindow, Ui_TestBench):
    version = 0.1
    file_prefs_name = "TestBench.prefs"
    current_dir = ""
    scene=None

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_TestBench.__init__(self)
        self.setupUi(self)
        self.statusbar.showMessage(
            "TestBench v{} - INSA Toulouse".format(self.version)
            )

        # Set close action
        self.action_Quit.triggered.connect(self.close)
        self.action_Quit.setIcon(QIcon("./img/close.png"))

        # Set open action
        self.action_Open.triggered.connect(self.open)
        self.action_Open.setIcon(QIcon("./img/open.png"))

        # Set save action
        self.action_Save.triggered.connect(self.open)
        self.action_Save.setIcon(QIcon("./img/save.png"))

    def message(self, text):
        self.messagesWidget.appendPlainText(text)

    def load_preferences(self):
        if os.path.exists(self.file_prefs_name):
            f = open(self.file_prefs_name, 'r')
            prefs = json.load(f)
            return prefs
        else:
            return None

    def save_preferences(self, prefs):
        f = open(self.file_prefs_name, 'w')
        json.dump(prefs, f)

    def open(self):
        fd = QFileDialog(self)
        fd.setNameFilter("Images (*.png *.xpm *.jpg)")
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
        last_dir = os.path.dirname(f)
        prefs['last_dir'] = last_dir
        self.save_preferences(prefs)
        self.current_dir = last_dir
        pmi = QGraphicsPixmapItem(QPixmap(f))
        if self.scene is None:
            self.scene = QGraphicsScene()
        self.scene.addItem(pmi)
        self.graphicsView.setScene(self.scene)

    def save(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.showMaximized()
    sys.exit(app.exec_())
