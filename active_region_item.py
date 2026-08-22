# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 01:03:54 2026

@author: Pinecone
"""

from region_item import RegionItem
from PySide6.QtGui import QColor, QPen, QBrush

class ActiveRegionItem(RegionItem):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        
        self.setPen(QPen(QColor("green")))
        self.setBrush(QBrush(QColor(0, 255, 0, 80)))