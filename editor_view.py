# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:33:36 2026

@author: Pinecone
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsView

class EditorView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.panning = False
        self.last_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            self.panning = True
            self.last_pos = event.position()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.panning:
            current_pos = event.position()
            delta = current_pos - self.last_pos
            
            dx, dy = delta.x(), delta.y()
            x_value = self.horizontalScrollBar().value()
            y_value = self.verticalScrollBar().value()

            self.horizontalScrollBar().setValue(int(x_value - dx))
            self.verticalScrollBar().setValue(int(y_value - dy))
            self.last_pos = current_pos
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            self.panning = False
            self.last_pos = None
        else:
            super().mouseReleaseEvent(event)
    
    def wheelEvent(self, event):
        zoom_factor = 1.15
        
        ''' 滑鼠滾輪往前滾: y > 0 '''
        if event.angleDelta().y() > 0:
            self.scale(zoom_factor, zoom_factor)
        else:
            self.scale(1 / zoom_factor, 1 / zoom_factor)