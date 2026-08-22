# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:02:03 2026

@author: Pinecone
"""

from editor_tool import EditorTool
from wall_item import WallItem

class WallTool(EditorTool):
    def __init__(self):
        self.wall = None
    
    def press(self, scene, event):
        p1 = event.scenePos()
        x, y = p1.x(), p1.y()
        
        self.wall = WallItem(x, y, x, y)
        scene.addItem(self.wall)
    
    def move(self, scene, event):
        if self.wall is not None:
            p1 = self.wall.line().p1()
            x1, y1 = p1.x(), p1.y()
            
            p2 = event.scenePos()
            x2, y2 = p2.x(), p2.y()
            self.wall.setLine(x1, y1, x2, y2)
    
    def release(self, scene, event):
        if self.wall is not None:
            p1 = self.wall.line().p1()
            x1, y1 = p1.x(), p1.y()
        
            p2 = event.scenePos()
            x2, y2 = p2.x(), p2.y()
        
            self.wall.setLine(x1, y1, x2, y2)
            self.wall = None