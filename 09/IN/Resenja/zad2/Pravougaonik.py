# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:33:03 2018

@author: Marko
"""

from GeometrijskaFigura import GeometrijskaFigura

class Pravougaonik(GeometrijskaFigura):

    def __init__(self, a, b):
        #super().__init__()
        self.__a = a
        self.__b = b
        
    def getA(self):
        return self.__a
    
    def setA(self, a):
        self.__a = a
    
    def getB(self):
        return self.__b
    
    def setB(self, b):
        self.__b = b
        
    def getObim(self):
        return 2 * (self.__a + self.__b)
    
    def getPovrsina(self):
        return self.__a * self.__b
        
    def __eq__(self, p2): #preklapanje operatora ==
        return self.__a == p2.__a and self.__b == p2.__b
        
    def __str__(self):
        return "Pravougaonik (a = " + str(self.__a) + ", b = " + str(self.__b) + ")"