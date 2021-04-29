# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:38:42 2018

@author: Marko
"""

class XCDStorage:
    
    def __init__(self):
        self.arhiva = []
        
    def add(self, cd):
        n = len(self.arhiva)
        for i in range(0, n):
            if self.arhiva[i] == cd:
                return False
        self.arhiva.append(cd)
        return True
        
    def remove(self, identif):
        n = len(self.arhiva)
        for i in range(0, n):
            if self.arhiva[i].id == identif:
                return self.arhiva.pop(i)
        return None
     
    def find(self, identif):
        n = len(self.arhiva)
        for i in range(0, n):
            if self.arhiva[i].id == identif:
                return self.arhiva[i]
        return None
            
    def clear(self):
        self.arhiva.clear()
        
    def __str__(self):
        n = len(self.arhiva)
        if n == 0:
            return "U arhivi nema diskova!"
        retVal = "Sadrzaj CD arhive je:\n"
        for i in range(0, n):
            retVal += str(self.arhiva[i]) + "\n" #veoma vazno: konvertovati objekat u string, jer nismo preklopili +
        return retVal