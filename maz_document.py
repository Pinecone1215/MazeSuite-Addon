# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:31:20 2026

@author: Pinecone
"""

import copy
import xml.etree.ElementTree as ET
from PySide6.QtCore import QLineF, QRectF

class MazDocument:
    blank_tree = ET.parse('maz_samples/blank.maz')
    ref_tree = ET.parse('maz_samples/geometry_reference.maz')
    
    ref_wall = ref_tree.find('MazeItems/Walls/Wall')
    ref_active_region = ref_tree.find('MazeItems/ActiveRegions/ActiveRegion')
    ref_end_region = ref_tree.find('MazeItems/EndRegions/EndRegion')
    
    def __init__(self):
        self.tree = copy.deepcopy(self.blank_tree)
        
        self.walls = self.tree.find('MazeItems/Walls')
        self.active_regions = self.tree.find('MazeItems/ActiveRegions')
        self.end_regions = self.tree.find('MazeItems/EndRegions')
        
        self.wall_id = 1
        self.regions = {
            'active': {
                'container': self.active_regions,
                'reference': self.ref_active_region,
                'id': 1,
                'group_id': 1,
                'group_prefix': 'active_region'
            },
        
            'end': {
                'container': self.end_regions,
                'reference': self.ref_end_region,
                'id': 1,
                'group_id': 1,
                'group_prefix': 'end_region'
            }
        }

    def add_wall(self, line: QLineF) -> None:
        x1 = line.x1()
        z1 = line.y1()
        x2 = line.x2()
        z2 = line.y2()
    
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
    
    def add_region(self, region_type: str, rectangles: list[QRectF]) -> None:
        region_info = self.regions[region_type]
    
        group = f"{region_info['group_prefix']}_{region_info['group_id']:02d}"
        region_info['group_id'] += 1
    
        for rect in rectangles:
            x1 = rect.left()
            x2 = rect.right()
            z1 = rect.top()
            z2 = rect.bottom()
    
            region = copy.deepcopy(region_info['reference'])
    
            region.set('id', str(region_info['id']))
            region.set('group', group)
    
            region_info['id'] += 1
    
            coord = region.find('MzCoord')
            coord.set('x1', str(x1))
            coord.set('x2', str(x2))
            coord.set('z1', str(z1))
            coord.set('z2', str(z2))
    
            region_info['container'].append(region)
        
    def write(self, path: str) -> None:
        self.tree.write(
            path,
            encoding='utf-8',
            xml_declaration=True
        )