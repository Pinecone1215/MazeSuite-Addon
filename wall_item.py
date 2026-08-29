# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:25:10 2026

@author: Pinecone
"""

import math
from PySide6.QtCore import QPointF
from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import QGraphicsLineItem, QGraphicsItem

class WallItem(QGraphicsLineItem):
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        super().__init__(x1, y1, x2, y2)
        
        self.setPen(QPen(QColor(205, 125, 45), 3))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    
    def angle(self) -> float:
        line = self.line()
        dx = line.x2() - line.x1()
        dy = line.y2() - line.y1()
        return math.degrees(math.atan2(dy, dx)) % 360
    
    def set_angle(self, value: float) -> None:
        line = self.line()
        x1, y1 = line.x1(), line.y1()
        x2, y2 = line.x2(), line.y2()
        
        ''' 畢氏定理計算斜邊長度 '''
        length = math.hypot(x2 - x1, y2 - y1)
        radian = math.radians(value)
        
        ''' 以 p1 為中心旋轉 line '''
        new_x2 = x1 + length * math.cos(radian)
        new_y2 = y1 + length * math.sin(radian)
        self.setLine(x1, y1, new_x2, new_y2)
    
    def scene_geometry(self) -> dict[str, float]:
        line = self.line()

        p1 = self.mapToScene(line.p1())
        p2 = self.mapToScene(line.p2())
        return {"x1": p1.x(), "y1": p1.y(), "x2": p2.x(), "y2": p2.y()}
    
    def set_scene_geometry(self, key: str, value: float) -> None:
        scene_geometry = self.scene_geometry()
        scene_geometry[key] = value
    
        p1_scene = QPointF(scene_geometry["x1"], scene_geometry["y1"])
        p2_scene = QPointF(scene_geometry["x2"], scene_geometry["y2"])
    
        p1_local = self.mapFromScene(p1_scene)
        p2_local = self.mapFromScene(p2_scene)
        self.setLine(p1_local.x(), p1_local.y(), p2_local.x(), p2_local.y())