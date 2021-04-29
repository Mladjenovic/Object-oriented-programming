# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:43:36 2018

@author: Marko
"""

class XCDStorageDict:
    
    def __init__(self):
        self.arhiva = {}
        
    def add(self, cd):
        if cd.id in self.arhiva:
            return False
        self.arhiva[cd.id] = cd
        return True
        
    def remove(self, identif):
        if identif in self.arhiva:
            return self.arhiva.pop(identif)
        return None
     
    def find(self, identif):
        if identif in self.arhiva:
            return self.arhiva[identif]
        return None
         
    def clear(self):
        self.arhiva.clear()
        
    def __str__(self):
        n = len(self.arhiva)
        if n == 0:
            return "U arhivi nema diskova!"
        retVal = "Sadrzaj CD arhive je:\n"
        for k in self.arhiva:
            retVal += str(self.arhiva[k]) + "\n" #veoma vazno: konvertovati objekat u string, jer nismo preklopili +
        return retVal