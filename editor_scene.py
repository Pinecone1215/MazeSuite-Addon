# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 01:06:23 2026

@author: Pinecone
"""

from grid_item import GridItem
from editor_tool import EditorTool
from PySide6.QtWidgets import QGraphicsScene

class EditorScene(QGraphicsScene):
    def __init__(self, x: float, y: float, w: float, h: float, grid_size: int, parent=None):
        super().__init__(parent)
        self.grid_size = grid_size
        
        '''
        setSceneRect(x, y, width, height):
        指定 Scene 可視世界的一個矩形範圍；前兩個是左上角，後兩個是寬高。
        '''
        self.setSceneRect(x, y, w, h)
        self.addItem(GridItem(x, y, w, h, self.grid_size))
        
        '''
        型別標註: editor_tool 預期只能是 EditorTool 類型，或是 None。
        '''
        self.editor_tool: EditorTool | None = None

    def mousePressEvent(self, event):
        if self.editor_tool is not None:
            self.editor_tool.press(self, event)
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.editor_tool is not None:
            self.editor_tool.move(self, event)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.editor_tool is not None:
            self.editor_tool.release(self, event)
        else:
            super().mouseReleaseEvent(event)
    
    def delete_selected_items(self):
        for item in self.selectedItems():
            self.removeItem(item)
            
    def clear_editor_items(self):
        for item in self.items():
            if not isinstance(item, GridItem):
                self.removeItem(item)