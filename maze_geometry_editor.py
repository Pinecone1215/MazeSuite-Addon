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
from editor_tool import EditorTool
from wall_tool import WallTool
from active_region_tool import ActiveRegionTool
from end_region_tool import EndRegionTool
from pointer_tool import PointerTool

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv) 

window = QMainWindow()
window.setWindowTitle('maze-geometry-editor')
window.resize(600, 400)

menu_bar = MenuBar(window)
window.setMenuBar(menu_bar)

tool_bar = ToolBar(window)
window.addToolBar(tool_bar)

view = EditorView(window)
scene = EditorScene(view)
view.setScene(scene)

def set_editor_tool(editor_tool: EditorTool | None):
    scene.editor_tool = editor_tool
    view.disable_pan()

tool_bar.pointer_action.triggered.connect(lambda: set_editor_tool(PointerTool()))
tool_bar.wall_action.triggered.connect(lambda: set_editor_tool(WallTool()))
tool_bar.active_region_action.triggered.connect(lambda: set_editor_tool(ActiveRegionTool()))
tool_bar.end_region_action.triggered.connect(lambda: set_editor_tool(EndRegionTool()))

tool_bar.pan_action.triggered.connect(lambda: (set_editor_tool(None), view.enable_pan()))

window.setCentralWidget(view)

window.show()
sys.exit(app.exec())