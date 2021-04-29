# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:56:31 2018

@author: Marko
"""

from abc import ABC, abstractmethod
 
class GeometrijskaFigura(ABC):
    
    """
    def __init__(self):
        super().__init__()
    """
    
    @abstractmethod
    def getObim(self):
        pass
    
    @abstractmethod
    def getPovrsina(self):
        pass