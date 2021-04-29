'''
Created on Oct 20, 2018

@author: Marko
'''

import zad1.Krug as krug
import zad1.Pravougaonik as pr

class Valjak:
    
    def __init__(self, r, h):
        self.b = krug.Krug(r)
        self.m = pr.Pravougaonik(self.b.getO(), h)

    def getR(self):
        return self.b.getR()
        
    def getH(self):
        return self.m.getB()
    
    def getP(self):
        return 2 * self.b.getP() * self.m.getP()
    
    def getV(self):
        return self.b.getP() * self.getH()

    def str(self):
        return "Valjak (r=" + str(self.b.getR()) + ", h=" + str(self.m.getB()) + ")"
    