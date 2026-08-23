# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:01:15 2026

@author: Pinecone
"""

class Item:
    def info(self) -> dict:
        raise NotImplementedError
    
    def set_info(self, key: str, value: float):
        raise NotImplementedError