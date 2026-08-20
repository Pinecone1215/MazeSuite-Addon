# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:02:03 2026

@author: Pinecone
"""

from drawing_tool import DrawingTool
from wall_item import WallItem

class WallTool(DrawingTool):
    def __init__(self):
        self.temp_wall = None
    
    def press(self, scene, event):
        p1 = event.scenePos()
        x, y = p1.x(), p1.y()
        
        self.temp_wall = WallItem(x, y, x, y)
        scene.addItem(self.temp_wall)
    
    def move(self, scene, event):
        if self.temp_wall is None:
            return
        
        p1 = self.temp_wall.line().p1()
        x1, y1 = p1.x(), p1.y()
        
        p2 = event.scenePos()
        x2, y2 = p2.x(), p2.y()
        
        self.temp_wall.setLine(x1, y1, x2, y2)
    
    def release(self, scene, event):
        if self.temp_wall is None:
            return
        
        p1 = self.temp_wall.line().p1()
        x1, y1 = p1.x(), p1.y()
        
        p2 = event.scenePos()
        x2, y2 = p2.x(), p2.y()
        
        scene.addItem(WallItem(x1, y1, x2, y2))
        scene.removeItem(self.temp_wall)
        
        self.temp_wall = None