# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:30:39 2026

@author: Pinecone
"""

from item import Item
from PySide6.QtWidgets import QDockWidget, QWidget, QFormLayout, QLabel

class PropertiesDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Properties", parent)
        self.current_item = None
    
        self.widget = QWidget()
        self.layout = QFormLayout(self.widget)
        self.setWidget(self.widget)
        
        self.setMinimumWidth(300)
    
    def set_item(self, item: Item | None):
        while self.layout.rowCount() > 0:
            self.layout.removeRow(0)
        
        if item is None:
            return
        
        data = item.info()
        for key, value in data.items():
            self.layout.addRow(QLabel(f'{key}'), QLabel(f'{value}'))