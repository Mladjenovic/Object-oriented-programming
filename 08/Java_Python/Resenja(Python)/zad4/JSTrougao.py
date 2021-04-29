'''
Created on Oct 20, 2018

@author: Marko
'''

from math import sqrt

class JSTrougao:
    
    def __init__(self, a):
        self.a = a

    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a
        
    def getO(self):
        return 3 * self.a
    
    def getP(self):
        s = self.getO() / 2
        return sqrt(s * pow((s - self.a), 3))

    def str(self):
        return "JSTrougao (a=" + str(self.a) + ")"
    