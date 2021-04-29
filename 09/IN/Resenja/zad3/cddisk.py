# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:31:18 2018

@author: Marko
"""

class CDDisk:
        
    def __init__(self, identif = -1, naziv = "nepoznat", izvodjac = "nepoznat"):
        self.id = identif
        self.naziv = naziv
        self.izvodjac = izvodjac
        
    def __eq__(self, cd2):
        if cd2 is None: # NIKAKO (zbog rekurzije): if cd2 == None:
            return False
        return self.id == cd2.id
        
    def __str__(self):
        return "CD [ " + str(self.id) + ", " + self.naziv + ", " + self.izvodjac + " ]"
        
    