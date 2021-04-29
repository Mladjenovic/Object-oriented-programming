'''
Created on Oct 20, 2018

@author: Marko
'''
from Krug import Krug
from Pravougaonik import Pravougaonik

class Valjak:
    
    def __init__(self, r, h):
        self.b = Krug(r)
        self.m = Pravougaonik(self.b.getO(), h)

    def getR(self):
        return self.b.getR()
        
    def getH(self):
        return self.m.getB()
    
    def getP(self):
        return 2 * self.b.getP() * self.m.getP()
    
    def getV(self):
        return self.b.getP() * self.getH()