# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:25:10 2026

@author: Pinecone
"""

from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import QGraphicsLineItem, QGraphicsItem

class WallItem(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        
        self.setPen(QPen(QColor(205, 125, 45), 3))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        