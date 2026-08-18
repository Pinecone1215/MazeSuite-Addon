# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:33:36 2026

@author: Pinecone
"""

from PySide6.QtWidgets import QGraphicsView

class EditorView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)