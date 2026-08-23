# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:33:24 2026

@author: Pinecone
"""

import sys
from menu_bar import MenuBar
from tool_bar import ToolBar
from PySide6.QtCore import Qt
from wall_tool import WallTool
from editor_tool import EditorTool
from editor_view import EditorView
from editor_scene import EditorScene
from pointer_tool import PointerTool
from end_region_tool import EndRegionTool
from properties_dock import PropertiesDock
from active_region_tool import ActiveRegionTool
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv) 

window = QMainWindow()
window.setWindowTitle('maze-geometry-editor')

menu_bar = MenuBar(window)
window.setMenuBar(menu_bar)

tool_bar = ToolBar(window)
window.addToolBar(tool_bar)

grid_size, snap_size = 20, 10

view = EditorView(window)
scene = EditorScene(view, grid_size)
view.setScene(scene)

properties_dock = PropertiesDock(window)
window.addDockWidget \
    (Qt.DockWidgetArea.RightDockWidgetArea, properties_dock)

def set_editor_tool(editor_tool: EditorTool | None):
    scene.editor_tool = editor_tool

set_editor_tool(PointerTool(snap_size))
tool_bar.pointer_action.triggered.connect(lambda: set_editor_tool(PointerTool(snap_size)))
tool_bar.wall_action.triggered.connect(lambda: set_editor_tool(WallTool(snap_size)))
tool_bar.active_region_action.triggered.connect(lambda: set_editor_tool(ActiveRegionTool(snap_size)))
tool_bar.end_region_action.triggered.connect(lambda: set_editor_tool(EndRegionTool(snap_size)))

menu_bar.delete_action.triggered.connect(scene.delete_selected_items)
window.setCentralWidget(view)

def update_properties():
    items = scene.selectedItems()
    properties_dock.set_item(items[0] if len(items) == 1 else None)
scene.changed.connect(update_properties)

window.showMaximized()
sys.exit(app.exec())