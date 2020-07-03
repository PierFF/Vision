from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsScene,\
     QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QPixmap
from image_tab_UI import Ui_image_tab
import sys


class SetFocusOnHover(QObject):
    def __init__(self):
        super(QObject, self).__init__()

    def eventFilter(self, object, event):
        if event.type() == QEvent.HoverEnter:
            object.setFocus()
        return super().eventFilter(object, event)


class ImageTab(QWidget, Ui_image_tab):
    scene = None
    image = None
    evtfil = SetFocusOnHover()

    message = pyqtSignal(str, name='message')

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Ui_image_tab.__init__(self)
        self.setupUi(self)
        self.graphicsView.installEventFilter(self.evtfil)

    def open(self, img_path):
        image = QPixmap(img_path)
        pixit = QGraphicsPixmapItem(image)
        if self.scene is None:
            self.scene = QGraphicsScene()
        self.scene.addItem(pixit)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        self.graphicsView.setFocus(Qt.MouseFocusReason)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tab = ImageTab()
    tab.show()
    sys.exit(app.exec_())
