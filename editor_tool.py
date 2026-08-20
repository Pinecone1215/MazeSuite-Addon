# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:12:48 2026

@author: Pinecone
"""

from abc import ABC, abstractmethod

class EditorTool(ABC):
    @abstractmethod
    def press(self, scene, event):
        pass

    @abstractmethod
    def move(self, scene, event):
        pass

    @abstractmethod
    def release(self, scene, event):
        pass