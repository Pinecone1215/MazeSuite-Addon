# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:33:24 2026

@author: Pinecone
"""

from editor_config import (
    GRID_SIZE, SNAP_SIZE, MIN_ITEM_SIZE,
    SCENE_X, SCENE_Y, SCENE_W, SCENE_H
)

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

from wall_item import WallItem
from active_region_item import ActiveRegionItem
from end_region_item import EndRegionItem
from maz_document import MazDocument

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv) 

window = QMainWindow()
window.setWindowTitle('maze-geometry-editor')

menu_bar = MenuBar(window)
window.setMenuBar(menu_bar)

tool_bar = ToolBar(window)
window.addToolBar(tool_bar)

view = EditorView(window)

scene = EditorScene(
    SCENE_X, SCENE_Y, SCENE_W, SCENE_H, 
    GRID_SIZE, view
)

view.setScene(scene)

properties_dock = PropertiesDock(window)
window.addDockWidget(
    Qt.DockWidgetArea.RightDockWidgetArea, properties_dock
)

def set_editor_tool(editor_tool: EditorTool | None):
    scene.editor_tool = editor_tool

set_editor_tool(PointerTool(SNAP_SIZE))
tool_bar.pointer_action.triggered.connect(
    lambda: set_editor_tool(
        PointerTool(SNAP_SIZE)
    )
)

tool_bar.wall_action.triggered.connect(
    lambda: set_editor_tool(
        WallTool(SNAP_SIZE, MIN_ITEM_SIZE)
    )
)

tool_bar.active_region_action.triggered.connect(
    lambda: set_editor_tool(
        ActiveRegionTool(SNAP_SIZE, MIN_ITEM_SIZE)
    )
)

tool_bar.end_region_action.triggered.connect(
    lambda: set_editor_tool(
        EndRegionTool(SNAP_SIZE, MIN_ITEM_SIZE)
    )
)

menu_bar.delete_action.triggered.connect(
    scene.delete_selected_items
)

window.setCentralWidget(view)

def update_selection():
    items = scene.selectedItems()
    
    properties_dock.set_item(
        items[0] if len(items) == 1 else None
    )

def update_properties():
    properties_dock.refresh()

scene.selectionChanged.connect(update_selection)
scene.changed.connect(update_properties)

def export_maz():
    document = MazDocument(0.1)
    
    for item in scene.items():
        if isinstance(item, WallItem):
            document.add_wall(item)
    
        elif isinstance(item, ActiveRegionItem):
            document.add_active_region(item)
    
        elif isinstance(item, EndRegionItem):
            document.add_end_region(item)
            
    document.write('maz_samples/output.maz')

menu_bar.export_action.triggered.connect(export_maz)

window.showMaximized()
sys.exit(app.exec())