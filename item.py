# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:01:15 2026

@author: Pinecone
"""

from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def info(self) -> dict:
        pass