# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 01:00:53 2026

@author: Pinecone
"""

from PySide6.QtCore import QPointF, QRectF
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsItem

class EndRegionItem(QGraphicsRectItem):
    def __init__(self, x1, y1, x2, y2):
        '''
        把兩個座標點轉成 QPointF，再建立 QRectF 並 normalized()，
        因此不論使用者往哪個方向拖曳，最後都會得到正常的矩形
        '''
        p1, p2 = QPointF(x1, y1), QPointF(x2, y2)
        rect = QRectF(p1, p2).normalized()
        
        super().__init__(rect)

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)