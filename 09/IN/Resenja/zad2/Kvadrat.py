# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:42:07 2018

@author: Marko
"""

from Pravougaonik import Pravougaonik

class Kvadrat(Pravougaonik):

    def __init__(self, a):
        super().__init__(a, a)
        
    def setA(self, a):
        super().setA(a)
        super().setB(a)
    
    def setB(self, b):
        super().setA(b)
        super().setB(b)
        
    def __str__(self):
        return "Kvadrat (a = " + str(super().getA()) + ")"