# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:59:41 2026

@author: Pinecone
"""

from editor_tool import EditorTool
from region_item import RegionItem
from PySide6.QtCore import QRectF, QPointF
from PySide6.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent

class RegionTool(EditorTool):
    item_class = RegionItem
    
    def __init__(self, snap_size: int, min_size: float):
        self.region = None
        self.start_pos = None
        
        self.snap_size = snap_size
        self.min_size = min_size
        
    def snap(self, pos: QPointF) -> QPointF:
        x = round(pos.x() / self.snap_size) * self.snap_size
        y = round(pos.y() / self.snap_size) * self.snap_size
        return QPointF(x, y)
        
    def press(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        self.start_pos = self.snap(event.scenePos())
        
        x, y = self.start_pos.x(), self.start_pos.y()
        self.region = self.item_class(x, y, 0, 0, self.min_size)
        scene.addItem(self.region)
        
    def move(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        if self.region is not None:
            p1 = self.start_pos
            p2 = self.snap(event.scenePos())
            rect = QRectF(p1, p2).normalized()
            self.region.setRect(rect)
        
    def release(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        if self.region is not None:
            p1 = self.start_pos
            p2 = self.snap(event.scenePos())
            rect = QRectF(p1, p2).normalized()
            
            self.region.setRect(rect)
            rect = self.region.rect()
            if rect.width() < self.min_size or rect.height() < self.min_size:
                scene.removeItem(self.region)
            
            self.region = None
            self.start_pos = None