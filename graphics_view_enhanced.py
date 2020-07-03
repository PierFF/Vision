from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt


class GraphicsViewEnhanced(QGraphicsView):

    def __init__(self, parent=None):
        super(QGraphicsView, self).__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAttribute(Qt.WA_Hover)

    def reset_view(self):
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

    def wheelEvent(self, event):
        # ---- Code from "weiwen" in found Stack Oveflow
        # ---- works very well

        # Zoom Factor
        zoomInFactor = 1.25
        zoomOutFactor = 0.8

        # Set Anchors
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.reset_view()
        elif event.key() == Qt.Key_Plus:
            self.scale(1.25, 1.25)
        elif event.key() == Qt.Key_Minus:
            self.scale(0.8, 0.8)

    def mouseDoubleClickEvent(self, event):
        self.reset_view()
