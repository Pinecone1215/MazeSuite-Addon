# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 01:06:23 2026

@author: Pinecone
"""

from PySide6.QtWidgets import QGraphicsScene
from editor_tool import EditorTool

class EditorScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        '''
        setSceneRect(x, y, width, height):
        指定 Scene 可視世界的一個矩形範圍；前兩個是左上角，後兩個是寬高。
        '''
        self.setSceneRect(-500, -500, 1000, 1000)
        
        '''
        型別標註: editor_tool 預期只能是 EditorTool 類型，或是 None。
        '''
        self.editor_tool: EditorTool | None = None

    def mousePressEvent(self, event):
        if self.editor_tool is not None:
            self.editor_tool.press(self, event)

    def mouseMoveEvent(self, event):
        if self.editor_tool is not None:
            self.editor_tool.move(self, event)

    def mouseReleaseEvent(self, event):
        if self.editor_tool is not None:
            self.editor_tool.release(self, event)