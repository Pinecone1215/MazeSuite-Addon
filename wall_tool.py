# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:02:03 2026

@author: Pinecone
"""

from wall_item import WallItem
from editor_tool import EditorTool
from PySide6.QtCore import QPointF

class WallTool(EditorTool):
    def __init__(self, grid_size: int = 5):
        self.wall = None
        self.grid_size = grid_size
        
    def snap(self, pos: QPointF) -> QPointF:
        x = round(pos.x() / self.grid_size) * self.grid_size
        y = round(pos.y() / self.grid_size) * self.grid_size
        return QPointF(x, y)
    
    def press(self, scene, event):
        p1 = self.snap(event.scenePos())
        x, y = p1.x(), p1.y()
        
        self.wall = WallItem(x, y, x, y)
        scene.addItem(self.wall)
    
    def move(self, scene, event):
        if self.wall is not None:
            p1 = self.wall.line().p1()
            x1, y1 = p1.x(), p1.y()
            
            p2 = self.snap(event.scenePos())
            x2, y2 = p2.x(), p2.y()
            self.wall.setLine(x1, y1, x2, y2)
    
    def release(self, scene, event):
        if self.wall is not None:
            p1 = self.wall.line().p1()
            x1, y1 = p1.x(), p1.y()
        
            p2 = self.snap(event.scenePos())
            x2, y2 = p2.x(), p2.y()
        
            self.wall.setLine(x1, y1, x2, y2)
            if self.wall.line().length() < self.grid_size:
                scene.removeItem(self.wall)
            self.wall = None