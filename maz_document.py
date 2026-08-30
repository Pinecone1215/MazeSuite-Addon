# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:31:20 2026

@author: Pinecone
"""

import copy
import xml.etree.ElementTree as ET
from PySide6.QtCore import QLineF, QRectF
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsLineItem

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

    def add_wall(self, wall_item: QGraphicsLineItem) -> None:
        line = wall_item.line()
        p1 = wall_item.mapToScene(line.p1())
        p2 = wall_item.mapToScene(line.p2())
        
        x1 = p1.x() * self.maz_scale
        z1 = p1.y() * self.maz_scale
        x2 = p2.x() * self.maz_scale
        z2 = p2.y() * self.maz_scale
        
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
    
    def approximate_region(self, region_item: QGraphicsRectItem) -> list[QRectF]:
        rect = region_item.rect()
        corners = [
            region_item.mapToScene(rect.topLeft()),
            region_item.mapToScene(rect.topRight()),
            region_item.mapToScene(rect.bottomRight()),
            region_item.mapToScene(rect.bottomLeft()),
        ]
        
        edges = [
            QLineF(corners[0], corners[1]),
            QLineF(corners[1], corners[2]),
            QLineF(corners[2], corners[3]),
            QLineF(corners[3], corners[0]),
        ]
        
        min_x = min(point.x() for point in corners)
        max_x = max(point.x() for point in corners)
        
        min_y = min(point.y() for point in corners)
        max_y = max(point.y() for point in corners)
        
        start_x = min_x - 1
        end_x = max_x + 1
        
        start_y = min_y
        end_y = max_y
        
        scan_line_up = QLineF(0, 0, 0, 0)
        scan_line_bottom = QLineF(0, 0, 0, 0)
        
        rectangles = []
        region_number = 50
        height = (end_y - start_y) / region_number

        for i in range(region_number):
            y_top = start_y + i * height
            y_bottom = min(y_top + height, end_y)
        
            scan_line_up.setLine(
                start_x, y_top,
                end_x, y_top
            )
        
            scan_line_bottom.setLine(
                start_x, y_bottom,
                end_x, y_bottom
            )
        
            top_x_points = []
            bottom_x_points = []
        
            for edge in edges:
                type_top, point_top = scan_line_up.intersects(edge)
                type_bottom, point_bottom = scan_line_bottom.intersects(edge)
        
                if type_top == QLineF.IntersectionType.BoundedIntersection:
                    top_x_points.append(point_top.x())
        
                if type_bottom == QLineF.IntersectionType.BoundedIntersection:
                    bottom_x_points.append(point_bottom.x())
        
            if len(top_x_points) < 2 or len(bottom_x_points) < 2:
                continue
        
            left_x = max(
                min(top_x_points),
                min(bottom_x_points)
            )
        
            right_x = min(
                max(top_x_points),
                max(bottom_x_points)
            )
        
            if left_x >= right_x:
                continue
        
            rectangles.append(
                QRectF(
                    left_x,
                    y_top,
                    right_x - left_x,
                    y_bottom - y_top
                )
            )
            
        return rectangles
        
    def add_active_region(self, region_item: QGraphicsRectItem) -> None:
        rectangles = self.approximate_region(region_item)
        for rect in rectangles:
            x1 = rect.left() * self.maz_scale
            x2 = rect.right() * self.maz_scale
            z1 = rect.top() * self.maz_scale
            z2 = rect.bottom() * self.maz_scale
            
            region = copy.deepcopy(self.ref_active_region)
            region.set('id', str(self.active_region_id))
            self.active_region_id += 1
        
            coord = region.find('MzCoord')
            coord.set('x1', str(x1))
            coord.set('x2', str(x2))
            coord.set('z1', str(z1))
            coord.set('z2', str(z2))
            self.active_regions.append(region)

    def add_end_region(self, region_item: QGraphicsRectItem) -> None:
        rectangles = self.approximate_region(region_item)
        for rect in rectangles:
            x1 = rect.left() * self.maz_scale
            x2 = rect.right() * self.maz_scale
            z1 = rect.top() * self.maz_scale
            z2 = rect.bottom() * self.maz_scale
            
            region = copy.deepcopy(self.ref_end_region)
            region.set('id', str(self.end_region_id))
            self.end_region_id += 1
        
            coord = region.find('MzCoord')
            coord.set('x1', str(x1))
            coord.set('x2', str(x2))
            coord.set('z1', str(z1))
            coord.set('z2', str(z2))
            self.end_regions.append(region)
        
    def write(self, path: str) -> None:
        self.tree.write(
            path,
            encoding='utf-8',
            xml_declaration=True
        )