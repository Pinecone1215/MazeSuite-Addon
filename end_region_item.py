# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 01:00:53 2026

@author: Pinecone
"""

from region_item import RegionItem

class EndRegionItem(RegionItem):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)