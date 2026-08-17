# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:43:44 2026

@author: Pinecone
"""

from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_file_menu()
        self.create_edit_menu()

    def create_file_menu(self):
        file_menu = self.addMenu("file")
        file_menu.addAction("new")
        file_menu.addAction("open")
        file_menu.addAction("save")
        file_menu.addAction("exit")

    def create_edit_menu(self):
        edit_menu = self.addMenu("edit")
        edit_menu.addAction("undo")
        edit_menu.addAction("redo")
        edit_menu.addAction("delete")
        