# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:33:24 2026

@author: Pinecone
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from menu_bar import MenuBar
from tool_bar import ToolBar
from editor_view import EditorView
from editor_scene import EditorScene
from wall_tool import WallTool

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv) 

window = QMainWindow()
window.setWindowTitle('maze-geometry-editor')
window.resize(600, 400)

window.setMenuBar(MenuBar(window))
window.addToolBar(ToolBar(window))

view = EditorView(window)
scene = EditorScene(view)

view.setScene(scene)
scene.editor_tool = WallTool()

window.setCentralWidget(view)

window.show()
sys.exit(app.exec())