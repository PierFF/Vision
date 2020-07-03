from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QTransform


class GraphicsViewEnhanced(QGraphicsView):

    mouse_click_pos = None
    zoom_scale = 1

    transformChanged = pyqtSignal(QTransform, name='transformChanged')

    def __init__(self, parent=None):
        super(QGraphicsView, self).__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAttribute(Qt.WA_Hover)

    def reset_view(self):
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        self.transformChanged.emit(self.transform())

    def zoom_in(self):
        self.scale(1.25, 1.25)
        self.zoom_scale *= 1.25
        self.transformChanged.emit(self.transform())

    def zoom_out(self):
        self.scale(0.8, 0.8)
        self.zoom_scale *= 0.8
        self.transformChanged.emit(self.transform())

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.reset_view()
        elif event.key() == Qt.Key_Plus:
            self.zoom_out()
        elif event.key() == Qt.Key_Minus:
            self.zoom_in()

    def mouseDoubleClickEvent(self, event):
        self.reset_view()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_click_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.mouse_click_pos is not None:
            dx = event.globalPos().x() - self.mouse_click_pos.x()
            dy = event.globalPos().y() - self.mouse_click_pos.y()
            if dx != 0 or dy != 0:
                self.centerOn()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_click_pos = None

