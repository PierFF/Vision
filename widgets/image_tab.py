from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsScene,\
     QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QPixmap
from widgets.UI.image_tab_UI import Ui_image_tab
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
    evt_filter_L = SetFocusOnHover()
    evt_filter_R = SetFocusOnHover()

    message = pyqtSignal(str, name='message')

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Ui_image_tab.__init__(self)
        self.setupUi(self)
        self.graphicsViewL.installEventFilter(self.evt_filter_L)
        self.graphicsViewR.installEventFilter(self.evt_filter_R)
        self.graphicsViewL.link_to(self.graphicsViewR)

    def open_in_graphicview(self, img_path, graphics_view):
        image = QPixmap(img_path)
        pixit = QGraphicsPixmapItem(image)
        if self.scene is None:
            self.scene = QGraphicsScene()
        self.scene.addItem(pixit)
        graphics_view.setScene(self.scene)
        graphics_view.fitInView(
            self.scene.sceneRect(), Qt.KeepAspectRatio)
        graphics_view.setFocus(Qt.MouseFocusReason)

    def open(self, img_path):
        self.open_in_graphicview(img_path, self.graphicsViewL)
        self.open_in_graphicview(img_path, self.graphicsViewR)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tab = ImageTab()
    tab.show()
    sys.exit(app.exec_())
