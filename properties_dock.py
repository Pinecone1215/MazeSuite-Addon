# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:30:39 2026

@author: Pinecone
"""

from editor_item import EditorItem
from PySide6.QtWidgets import QDockWidget, QWidget, QFormLayout, QDoubleSpinBox

class PropertiesDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Properties", parent)
    
        self.widget = QWidget()
        self.layout = QFormLayout(self.widget)
        self.setWidget(self.widget)
        
        self.setMinimumWidth(300)
        
        self.item = None
        self.fields = {}
    
    def clear(self):
        self.fields.clear()
        while self.layout.rowCount() > 0:
            self.layout.removeRow(0)
    
    def refresh(self):
        if self.item is None:
            return
    
        data = self.item.info()
        for key, value in data.items():
            self.fields[key].blockSignals(True)
            self.fields[key].setValue(value)
            self.fields[key].blockSignals(False)
    
    def set_item(self, item: EditorItem | None):
        if item is self.item:
            return
        
        self.item = item
        self.clear()
        
        if item is None:
            return
        
        for key, value in item.info().items():
            field = QDoubleSpinBox()
            field.setRange(-3000, 3000)
            field.setValue(value)

            field.valueChanged.connect \
                (lambda value, key=key: self.item.set_info(key, value))

            self.fields[key] = field
            self.layout.addRow(key, field)