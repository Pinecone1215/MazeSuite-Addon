# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:31:20 2026

@author: Pinecone
"""

import copy
from editor_item import EditorItem
import xml.etree.ElementTree as ET

class MazDocument:
    blank_tree = ET.parse('maz_samples/blank.maz')
    ref_tree = ET.parse('maz_samples/geometry_reference.maz')
    
    ref_wall = ref_tree.find('MazeItems/Walls/Wall')
    ref_active_region = ref_tree.find('MazeItems/ActiveRegions/ActiveRegion')
    ref_end_region = ref_tree.find('MazeItems/EndRegions/EndRegion')
    
    def __init__(self, maz_scale: float):
        self.maz_scale = maz_scale
        self.tree = copy.deepcopy(self.blank_tree)
        
        self.walls = self.tree.find('MazeItems/Walls')
        self.active_regions = self.tree.find('MazeItems/ActiveRegions')
        self.end_regions = self.tree.find('MazeItems/EndRegions')
        
        self.wall_id = 1
        self.active_region_id = 1
        self.end_region_id = 1
    
    # TODO: EditorItem 太泛，後續有需要再細分介面。
    def add_wall(self, wall_item: EditorItem) -> None:
        geometry: dict[str, float] = wall_item.scene_geometry()
        x1 = geometry['x1'] * self.maz_scale
        z1 = geometry['y1'] * self.maz_scale
        x2 = geometry['x2'] * self.maz_scale
        z2 = geometry['y2'] * self.maz_scale
        
        wall = copy.deepcopy(self.ref_wall)
        wall.set('id', str(self.wall_id))
        self.wall_id += 1
        
        point1 = wall.find('MzPoint1')
        point2 = wall.find('MzPoint2')
        point3 = wall.find('MzPoint3')
        point4 = wall.find('MzPoint4')
        
        point1.set('x', str(x1))
        point1.set('z', str(z1))
        
        point2.set('x', str(x1))
        point2.set('z', str(z1))
        
        point3.set('x', str(x2))
        point3.set('z', str(z2))
        
        point4.set('x', str(x2))
        point4.set('z', str(z2))
        
        self.walls.append(wall)