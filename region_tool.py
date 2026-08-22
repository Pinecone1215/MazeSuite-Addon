# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:59:41 2026

@author: Pinecone
"""

from PySide6.QtCore import QRectF
from PySide6.QtCore import QPointF
from editor_tool import EditorTool
from region_item import RegionItem

class RegionTool(EditorTool):
    item_class = RegionItem
    
    def __init__(self, grid_size: int = 5):
        self.region = None
        self.start_pos = None
        self.grid_size = grid_size
        
    def snap(self, pos: QPointF) -> QPointF:
        x = round(pos.x() / self.grid_size) * self.grid_size
        y = round(pos.y() / self.grid_size) * self.grid_size
        return QPointF(x, y)
        
    def press(self, scene, event):
        self.start_pos = self.snap(event.scenePos())
        
        x, y = self.start_pos.x(), self.start_pos.y()
        self.region = self.item_class(x, y, x, y)
        scene.addItem(self.region)
        
    def move(self, scene, event):
        if self.region is not None:
            p1 = self.start_pos
            p2 = self.snap(event.scenePos())
            rect = QRectF(p1, p2).normalized()
            self.region.setRect(rect)
        
    def release(self, scene, event):
        if self.region is not None:
            p1 = self.start_pos
            p2 = self.snap(event.scenePos())
            rect = QRectF(p1, p2).normalized()
            
            self.region.setRect(rect)
            rect = self.region.rect()
            if rect.width() < self.grid_size or rect.height() < self.grid_size:
                scene.removeItem(self.region)
            
            self.region = None
            self.start_pos = None