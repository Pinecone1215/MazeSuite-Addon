# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:25:10 2026

@author: Pinecone
"""

from item import Item
from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import QGraphicsLineItem, QGraphicsItem

class WallItem(QGraphicsLineItem, Item):
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        super().__init__(x1, y1, x2, y2)
        
        self.setPen(QPen(QColor(205, 125, 45), 3))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    
    def info(self) -> dict:
        line = self.line()
        p1 = self.mapToScene(line.p1())
        p2 = self.mapToScene(line.p2())
        
        x1, y1 = p1.x(), p1.y()
        x2, y2 = p2.x(), p2.y()
        
        data = {'x1' : x1, 'y1' : y1, 'x2' : x2, 'y2' : y2}
        return data
    
    def set_info(self, key: str, value: float):
        data = self.info()
        data[key] = value
    
        self.setPos(0, 0)
        self.setLine(data["x1"], data["y1"], data["x2"], data["y2"])