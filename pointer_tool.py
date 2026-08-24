# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:06:28 2026

@author: Pinecone
"""

from editor_tool import EditorTool
from PySide6.QtCore import QPointF
from PySide6.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent

class PointerTool(EditorTool):
    def __init__(self, snap_size: int = 5):
        self.snap_size = snap_size
    
    def snap(self, pos: QPointF) -> QPointF:
        x = round(pos.x() / self.snap_size) * self.snap_size
        y = round(pos.y() / self.snap_size) * self.snap_size
        return QPointF(x, y)
    
    def press(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        QGraphicsScene.mousePressEvent(scene, event)

    def move(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        QGraphicsScene.mouseMoveEvent(scene, event)
        for item in scene.selectedItems():
            item.setPos(self.snap(item.pos()))

    def release(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        QGraphicsScene.mouseReleaseEvent(scene, event)