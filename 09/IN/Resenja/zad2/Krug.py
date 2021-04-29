# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:04:30 2018

@author: Marko
"""

from GeometrijskaFigura import GeometrijskaFigura
import math as m

class Krug(GeometrijskaFigura):

    def __init__(self, r):
        super().__init__()
        self.__r = r
        
    def getR(self):
        return self.__r
    
    def setR(self, r):
        self.__r = r
    
    def getObim(self):
        return 2 * self.__r * m.pi
    
    def getPovrsina(self):
        return self.__r ** 2 * m.pi
        #return m.pow(self.__r, 2) * m.pi
        
    def __add__(self, krug2): #preklapanje operatora +
        return Krug(self.__r + krug2.__r)
        
    def __str__(self):
        return "Krug (r = " + str(self.__r) + ")"