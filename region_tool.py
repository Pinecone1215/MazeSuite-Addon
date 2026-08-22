# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:59:41 2026

@author: Pinecone
"""

from PySide6.QtCore import QRectF
from editor_tool import EditorTool
from region_item import RegionItem

class RegionTool(EditorTool):
    item_class = RegionItem
    
    def __init__(self):
        self.region = None
        self.start_pos = None
        
    def press(self, scene, event):
        self.start_pos = event.scenePos()
        
        x, y = self.start_pos.x(), self.start_pos.y()
        self.region = self.item_class(x, y, x, y)
        scene.addItem(self.region)
        
    def move(self, scene, event):
        if self.region is not None:
            p1 = self.start_pos
            p2 = event.scenePos()
            rect = QRectF(p1, p2).normalized()
            self.region.setRect(rect)
        
    def release(self, scene, event):
        if self.region is not None:
            p1 = self.start_pos
            p2 = event.scenePos()
            rect = QRectF(p1, p2).normalized()
            
            self.region.setRect(rect)
            self.region = None
            self.start_pos = None