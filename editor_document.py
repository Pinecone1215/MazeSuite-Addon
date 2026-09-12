# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:43:59 2026

@author: Pinecone
"""

from editor_config import MIN_ITEM_SIZE
from collections.abc import Callable

import xml.etree.ElementTree as ET

from wall_item import WallItem
from region_item import RegionItem
from editor_scene import EditorScene
from end_region_item import EndRegionItem
from active_region_item import ActiveRegionItem

class EditorDocument:
    def __init__(self, scene: EditorScene):
        self.scene = scene
        
        self.tags = {
            WallItem: "wall",
            ActiveRegionItem: "active_region",
            EndRegionItem: "end_region",
        }
        
        self.writers: dict[type, Callable] = {
            WallItem: self.write_wall,
            ActiveRegionItem: self.write_region,
            EndRegionItem: self.write_region
        }
        
        self.readers = {
            "wall": self.read_wall,
            "active_region": lambda e: self.read_region(e, ActiveRegionItem),
            "end_region": lambda e: self.read_region(e, EndRegionItem),
        }
        
    def read(self, path: str):
        tree = ET.parse(path)
        root = tree.getroot()
        
        if root.tag != "maze_geometry_editor":
            raise ValueError("Invalid AMAZ document")
        
        items_element = root.find("items")
        
        if items_element is None:
            raise ValueError("Invalid AMAZ document: missing <items>")
        
        loaded_items: list[WallItem | RegionItem] = []
        for element in items_element:
            if element.tag not in self.readers:
                continue
            
            reader = self.readers[element.tag]
            loaded_items.append(reader(element))
        
        self.scene.clear_editor_items()
        for item in loaded_items:
            self.scene.addItem(item)
        
    def write(self, path: str):
        root = ET.Element("maze_geometry_editor", {"version": "1.0"})
        items_element = ET.SubElement(root, "items")
        
        for item in self.scene.items():
            item_type = type(item)
            if item_type not in self.writers:
                continue
            
            writer = self.writers[item_type]
            writer(items_element, item)
        
        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")
        
        tree.write(
            path,
            encoding="utf-8",
            xml_declaration=True
        )
        
    def read_wall(self, element: ET.Element) -> WallItem:
        x1 = float(element.get("x1"))
        y1 = float(element.get("y1"))
        x2 = float(element.get("x2"))
        y2 = float(element.get("y2"))
        return WallItem(x1, y1, x2, y2, MIN_ITEM_SIZE)
    
    def read_region(
        self,
        element: ET.Element,
        item_type: type[RegionItem]
    ):
        x = float(element.get("x"))
        y = float(element.get("y"))
        width = float(element.get("width"))
        height = float(element.get("height"))
        angle = float(element.get("angle"))
    
        item = item_type(x, y, width, height, MIN_ITEM_SIZE)
        item.set_angle(angle)
        return item
        
    def write_wall(self, parent: ET.Element, item: WallItem):
        geometry = item.scene_geometry()
        x1, y1 = geometry['x1'], geometry['y1']
        x2, y2 =  geometry['x2'], geometry['y2']
    
        ET.SubElement(
            parent,
            self.tags[type(item)],
            {
                "x1": str(x1),
                "y1": str(y1),
                "x2": str(x2),
                "y2": str(y2),
            }
        )
        
    def write_region(self, parent: ET.Element, item: RegionItem):
        geometry = item.scene_geometry()
        x, y = geometry['x'], geometry['y']
        width, height = geometry['width'], geometry['height']
    
        ET.SubElement(
            parent,
            self.tags[type(item)],
            {
                "x": str(x),
                "y": str(y),
                "width": str(width),
                "height": str(height),
                "angle": str(item.angle()),
            }
        )