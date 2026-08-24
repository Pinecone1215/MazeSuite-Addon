# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:01:15 2026

@author: Pinecone
"""

from typing import Protocol, runtime_checkable

@runtime_checkable
class EditorItem(Protocol):
    def angle(self) -> float:
        ...
    
    def set_angle(self, value: float) -> None:
        ...
    
    def geometry(self) -> dict[str, float]:
        ...
    
    def set_geometry(self, key: str, value: float) -> None:
        ...
    
    def scene_geometry(self) -> dict[str, float]:
        ...
    
    def set_scene_geometry(self, key: str, value: float) -> None:
        ...