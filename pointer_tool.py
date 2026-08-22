# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:39:00 2026

@author: Pinecone
"""

from editor_tool import EditorTool
from PySide6.QtWidgets import QGraphicsScene

class PointerTool(EditorTool):
    def press(self, scene, event):
        QGraphicsScene.mousePressEvent(scene, event)

    def move(self, scene, event):
        QGraphicsScene.mouseMoveEvent(scene, event)

    def release(self, scene, event):
        QGraphicsScene.mouseReleaseEvent(scene, event)