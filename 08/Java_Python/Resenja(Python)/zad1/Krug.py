'''
Created on Oct 20, 2018

@author: Marko
'''
class Krug:
    
    def __init__(self, r):
        self.r = r

    def getR(self):
        return self.r

    def setR(self, r):
        self.r = r
        
    def getO(self):
        return 2 * self.r * 3.14
    
    def getP(self):
        return self.r * self.r * 3.14

    def str(self):
        return "Krug (r=" + str(self.r) + ")"
    