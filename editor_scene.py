# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 01:06:23 2026

@author: Pinecone
"""

from PySide6.QtWidgets import QGraphicsScene, QGraphicsItem

class EditorScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        '''
        setSceneRect(x, y, width, height):
        指定 Scene 可視世界的一個矩形範圍；前兩個是左上角，後兩個是寬高。
        '''
        self.setSceneRect(-500, -500, 1000, 1000)
        
        ''' 測試繪製矩形 '''
        self.rectangle = self.addRect(-50, -50, 100, 100)
        
        ''' 測試選取圖形 '''
        self.rectangle.setFlag(
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
        )