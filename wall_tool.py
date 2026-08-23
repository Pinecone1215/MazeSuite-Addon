# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:02:03 2026

@author: Pinecone
"""

from wall_item import WallItem
from editor_tool import EditorTool
from PySide6.QtCore import QPointF
from PySide6.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent

class WallTool(EditorTool):
    def __init__(self, snap_size: int = 5):
        self.wall = None
        self.snap_size = snap_size
        
    def snap(self, pos: QPointF) -> QPointF:
        x = round(pos.x() / self.snap_size) * self.snap_size
        y = round(pos.y() / self.snap_size) * self.snap_size
        return QPointF(x, y)
    
    def press(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        p1 = self.snap(event.scenePos())
        x, y = p1.x(), p1.y()
        
        self.wall = WallItem(x, y, x, y)
        scene.addItem(self.wall)
    
    def move(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        if self.wall is not None:
            p1 = self.wall.line().p1()
            x1, y1 = p1.x(), p1.y()
            
            p2 = self.snap(event.scenePos())
            x2, y2 = p2.x(), p2.y()
            self.wall.setLine(x1, y1, x2, y2)
    
    def release(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        if self.wall is not None:
            p1 = self.wall.line().p1()
            x1, y1 = p1.x(), p1.y()
        
            p2 = self.snap(event.scenePos())
            x2, y2 = p2.x(), p2.y()
        
            self.wall.setLine(x1, y1, x2, y2)
            if self.wall.line().length() < self.snap_size:
                scene.removeItem(self.wall)
            self.wall = None