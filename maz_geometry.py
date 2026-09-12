# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:06:17 2026

@author: Pinecone
"""

import math
from typing import TypeAlias
from collections.abc import Callable

from wall_item import WallItem
from end_region_item import EndRegionItem
from active_region_item import ActiveRegionItem

from PySide6.QtCore import QLineF, QRectF
from PySide6.QtWidgets import QGraphicsScene

from PySide6.QtWidgets import (
    QGraphicsItem,
    QGraphicsLineItem,
    QGraphicsRectItem
)

class MazGeometry:
    Geometry: TypeAlias = QLineF | list[QRectF]
    Processor: TypeAlias = Callable[..., Geometry]
    
    @staticmethod
    def process_line(
            line_item: QGraphicsLineItem, 
            maz_scale: float
        ) -> QLineF:
        
        line = line_item.line()
        p1 = line_item.mapToScene(line.p1())
        p2 = line_item.mapToScene(line.p2())
        
        return QLineF(
            p1.x() * maz_scale,
            p1.y() * maz_scale,
            p2.x() * maz_scale,
            p2.y() * maz_scale
        )
    
    @staticmethod
    def process_rect(
            rect_item: QGraphicsRectItem, 
            maz_scale: float
        ) -> list[QRectF]:
        
        rect = rect_item.rect()
        corners = [
            rect_item.mapToScene(rect.topLeft()),
            rect_item.mapToScene(rect.topRight()),
            rect_item.mapToScene(rect.bottomRight()),
            rect_item.mapToScene(rect.bottomLeft()),
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
        
        rectangles: list[QRectF] = []
        
        slice_height = 3
        slice_count = math.ceil((end_y - start_y) / slice_height)

        for i in range(slice_count):
            y_top = start_y + i * slice_height
            y_bottom = min(y_top + slice_height, end_y)
        
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
            
            scaled_rect = QRectF(
                left_x * maz_scale,
                y_top * maz_scale,
                (right_x - left_x) * maz_scale,
                (y_bottom - y_top) * maz_scale
            )
            
            rectangles.append(scaled_rect)
            
        return rectangles
        
    processors: dict[type[QGraphicsItem], Processor] = {
        WallItem: process_line,
        EndRegionItem: process_rect,
        ActiveRegionItem: process_rect
    }
    
    def __init__(self, scene: QGraphicsScene, maz_scale: float):
        self.items: dict[
            type[QGraphicsItem],
            list[MazGeometry.Geometry]
        ] = { item_type: [] for item_type in MazGeometry.processors }
        
        for item in scene.items():
            item_type = type(item)
            if item_type not in MazGeometry.processors:
                continue
            
            processor = MazGeometry.processors[item_type]
            processed_item = processor(item, maz_scale)
            self.items[item_type].append(processed_item)