# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:12:48 2026

@author: Pinecone
"""

from abc import ABC, abstractmethod
from PySide6.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent

class EditorTool(ABC):
    @abstractmethod
    def press(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        pass

    @abstractmethod
    def move(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        pass

    @abstractmethod
    def release(self, scene: QGraphicsScene, event: QGraphicsSceneMouseEvent):
        pass