# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:51:15 2026

@author: Pinecone
"""

from editor_item import EditorItem
from PySide6.QtCore import QPointF, QRectF
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsItem

class RegionItem(QGraphicsRectItem, EditorItem):
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        '''
        把兩個座標點轉成 QPointF，再建立 QRectF 並 normalized()，
        因此不論使用者往哪個方向拖曳，最後都會得到正常的矩形
        '''
        p1, p2 = QPointF(x1, y1), QPointF(x2, y2)
        rect = QRectF(p1, p2).normalized()
        
        super().__init__(rect)

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    
    def info(self) -> dict:
        rect = self.rect()
        p1 = self.mapToScene(rect.topLeft())
        p2 = self.mapToScene(rect.bottomRight())
        
        x1, y1 = p1.x(), p1.y()
        x2, y2 = p2.x(), p2.y()
        
        data = {'x1' : x1, 'y1' : y1, 'x2' : x2, 'y2' : y2}
        return data
    
    def set_info(self, key: str, value: float):
        data = self.info()
        data[key] = value
    
        p1 = QPointF(data["x1"], data["y1"])
        p2 = QPointF(data["x2"], data["y2"])
    
        self.setPos(0, 0)
        self.setRect(QRectF(p1, p2).normalized())
    
    def apply_position(self):
        data = self.info()
    
        p1 = QPointF(data["x1"], data["y1"])
        p2 = QPointF(data["x2"], data["y2"])
    
        self.setPos(0, 0)
        self.setRect(QRectF(p1, p2).normalized())