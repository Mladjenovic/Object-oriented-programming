'''
Created on Oct 20, 2018

@author: Marko
'''

from JSTrougao import JSTrougao
from Pravougaonik import Pravougaonik

class PP3Prizma:
    
    def __init__(self, a, h):
        self.b = JSTrougao(a)
        self.m = Pravougaonik(self.b.getO(), h)

    def getA(self):
        return self.b.getA()
        
    def getH(self):
        return self.m.getB()
    
    def getP(self):
        return 2 * self.b.getP() + self.m.getP()
    
    def getV(self):
        return self.b.getP() * self.getH()