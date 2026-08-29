# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:30:39 2026

@author: Pinecone
"""

from PySide6.QtWidgets import (
    QDockWidget, QWidget, QFormLayout, QDoubleSpinBox
)

from editor_item import EditorItem

class PropertiesDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Properties", parent)
    
        self.widget = QWidget()
        self.layout = QFormLayout(self.widget)
        self.setWidget(self.widget)
        
        self.setMinimumWidth(300)
        
        self.item: EditorItem | None = None
        self.fields: dict[str, QDoubleSpinBox] = {}
    
    def clear(self):
        self.fields.clear()
        while self.layout.rowCount() > 0:
            self.layout.removeRow(0)
    
    def refresh(self):
        if self.item is None:
            return
    
        scene_geometry = self.item.scene_geometry()
        for key, value in scene_geometry.items():
            self.fields[key].blockSignals(True)
            self.fields[key].setValue(value)
            self.fields[key].blockSignals(False)
        
        angle = self.item.angle()
        self.fields["angle"].blockSignals(True)
        self.fields["angle"].setValue(angle)
        self.fields["angle"].blockSignals(False)
        
    def on_geometry_changed(self, key: str, value: float) -> None:
        self.item.set_scene_geometry(key, value)
    
    def set_item(self, item: EditorItem | None):
        if item is self.item:
            return
        
        self.item = item
        self.clear()
        
        if item is None:
            return
        
        scene_geometry = self.item.scene_geometry()
        for key, value in scene_geometry.items():
            field = QDoubleSpinBox()
            field.setRange(-3000, 3000)
            field.setValue(value)
            
            field.valueChanged.connect(
                lambda value, key=key: 
                    self.on_geometry_changed(key, value)
            )

            self.fields[key] = field
            self.layout.addRow(key, field)
        
        angle = self.item.angle()
        field = QDoubleSpinBox()
        field.setRange(0, 360)
        field.setValue(angle)
        
        field.valueChanged.connect(
            lambda value: self.item.set_angle(value)
        )
        
        key = 'angle'
        self.fields[key] = field
        self.layout.addRow(key, field)