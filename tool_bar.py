# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:02:07 2026

@author: Pinecone
"""

from PySide6.QtWidgets import QToolBar

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pointer_action = self.addAction("pointer")
        self.wall_action = self.addAction("wall")
        self.end_region_action = self.addAction("end region")
        self.active_region_action = self.addAction("active region")