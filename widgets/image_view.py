from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QTransform


class ImageView(QGraphicsView):

    mouse_click_pos = None
    zoom_scale = 1

    viewChanged = pyqtSignal(QTransform, name='viewChanged')
    linked_image_view = None

    def __init__(self, parent=None):
        super(QGraphicsView, self).__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setAttribute(Qt.WA_Hover)
        self.setDragMode(self.ScrollHandDrag)
        self.setTransformationAnchor(self.AnchorUnderMouse)

    def link_to(self, other):
        self.linked_image_view = other
        other.linked_image_view = self
        self.viewChanged.connect(
            other.setView)
        other.viewChanged.connect(
            self.setView)

        self.verticalScrollBar().valueChanged.connect(
            other.verticalScrollBar().setValue
        )
        other.verticalScrollBar().valueChanged.connect(
            self.verticalScrollBar().setValue
        )
        self.horizontalScrollBar().valueChanged.connect(
            other.horizontalScrollBar().setValue
        )
        other.horizontalScrollBar().valueChanged.connect(
            self.horizontalScrollBar().setValue
        )

    def setView(self, transform):
        self.setTransform(transform)
        if self. linked_image_view is not None:
            self.horizontalScrollBar().setValue(
                self.linked_image_view.horizontalScrollBar().value()
                )
            self.verticalScrollBar().setValue(
                self.linked_image_view.verticalScrollBar().value()
                )

    def reset_view(self):
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        self.viewChanged.emit(self.transform())

    def zoom_in(self):
        self.scale(1.25, 1.25)
        self.zoom_scale *= 1.25
        self.viewChanged.emit(self.transform())

    def zoom_out(self):
        self.scale(0.8, 0.8)
        self.zoom_scale *= 0.8
        self.viewChanged.emit(self.transform())

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()
        super().wheelEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.reset_view()
        elif event.key() == Qt.Key_Plus:
            self.zoom_in()
        elif event.key() == Qt.Key_Minus:
            self.zoom_out()
        super().keyPressEvent(event)

    def mouseDoubleClickEvent(self, event):
        self.reset_view()
        super().mouseDoubleClickEvent(event)
