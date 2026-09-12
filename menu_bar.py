# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:43:44 2026

@author: Pinecone
"""

from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction, QKeySequence

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.delete_action = QAction("Delete", self)
        self.delete_action.setShortcut(
            QKeySequence(QKeySequence.StandardKey.Delete)
        )
        
        self.export_action = QAction("export to .maz", self)
        
        self.open_action = QAction("open", self)
        self.save_action = QAction("save", self)
        
        self.open_action.setShortcut(
            QKeySequence(QKeySequence.StandardKey.Open)
        )

        self.save_action.setShortcut(
            QKeySequence(QKeySequence.StandardKey.Save)
        )
        
        self.create_file_menu()
        self.create_edit_menu()

    def create_file_menu(self):
        file_menu = self.addMenu("file")
        file_menu.addAction("new")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.export_action)
        file_menu.addAction("exit")

    def create_edit_menu(self):
        edit_menu = self.addMenu("edit")
        edit_menu.addAction("undo")
        edit_menu.addAction("redo")
        edit_menu.addAction(self.delete_action)
        