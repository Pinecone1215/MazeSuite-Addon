# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 01:11:38 2026

@author: Pinecone
"""

import math
from PySide6.QtGui import QPen, QColor
from PySide6.QtWidgets import QGraphicsItem
from PySide6.QtCore import QRectF, QLineF, Qt

class GridItem(QGraphicsItem):
    ''' 目前尺寸由程式內部控制，暫時不需要防呆 '''
    def __init__(self, left: float, top: float, width: float, height: float, grid_size: int):
        super().__init__()
        self.grid_size = grid_size
        self.rect = QRectF(left, top, width, height)
        
        self.setZValue(-1000)
        self.setAcceptedMouseButtons(Qt.MouseButton.NoButton)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemUsesExtendedStyleOption, True)
    
    ''' QGraphicsItem 子類必須實作的 function '''
    def boundingRect(self) -> QRectF:
        return self.rect
    
    def paint(self, painter, option, widget=None):
        pen = QPen(QColor(255, 255, 255, 127))
        pen.setWidthF(0.5)
        pen.setStyle(Qt.PenStyle.DashLine)
        
        painter.setPen(pen)
        exposed_rect = option.exposedRect
        
        left = math.floor(exposed_rect.left() / self.grid_size) * self.grid_size
        top = math.floor(exposed_rect.top() / self.grid_size) * self.grid_size
        right, bottom = math.floor(exposed_rect.right()), math.floor(exposed_rect.bottom())
        
        vertical_lines, horizontal_lines = \
            [QLineF(x, top, x, bottom) for x in range(left, right + 1, self.grid_size)], \
            [QLineF(left, y, right, y) for y in range(top, bottom + 1, self.grid_size)]
        
        painter.drawLines(vertical_lines)
        painter.drawLines(horizontal_lines)