# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:51:15 2026

@author: Pinecone
"""

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsItem

class RegionItem(QGraphicsRectItem):
    def __init__(self, x: float, y: float, w: float, h: float, min_size: float):
        super().__init__(x, y, w, h)
        
        self.min_size = min_size
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    
    ''' QGraphicsRectItem.rotation() 的數值沒有上下限 '''
    def angle(self) -> float:
        return self.rotation() % 360
    
    def set_angle(self, value: float) -> None:
        self.setTransformOriginPoint(self.rect().topLeft())
        self.setRotation(value)
    
    def scene_geometry(self) -> dict[str, float]:
        rect = self.rect()
        p = self.mapToScene(rect.topLeft())
        
        return {
            "x": p.x(), "y": p.y(), 
            "width": rect.width(), "height": rect.height()
        }
    
    def set_scene_geometry(self, key: str, value: float) -> None:
        scene_geometry = self.scene_geometry()

        if key == "x":
            dx = value - scene_geometry["x"]
            self.moveBy(dx, 0)
    
        elif key == "y":
            dy = value - scene_geometry["y"]
            self.moveBy(0, dy)
    
        elif key == "width" and value >= self.min_size:
            rect = self.rect()
            rect.setWidth(value)
            self.setRect(rect)
        
        elif key == "height" and value >= self.min_size:
            rect = self.rect()
            rect.setHeight(value)
            self.setRect(rect)