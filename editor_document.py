# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:43:59 2026

@author: Pinecone
"""

from collections.abc import Callable

import xml.etree.ElementTree as ET

from wall_item import WallItem
from region_item import RegionItem, ActiveRegionItem, EndRegionItem

class EditorDocument:
    def __init__(self, scene):
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
        
    def write_wall(self, parent: ET.Element, item: WallItem):
        x1, y1, x2, y2 = item.scene_geometry()
    
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
        x, y, width, height = item.scene_geometry()
    
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