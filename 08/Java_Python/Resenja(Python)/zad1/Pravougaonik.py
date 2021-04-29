'''
Created on Oct 20, 2018

@author: Marko
'''
class Pravougaonik:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getA(self):
        return self.a
    
    def getB(self):
        return self.b

    def setA(self, a):
        self.a = a
        
    def setB(self, b):
        self.b = b
                
    def getO(self):
        return 2 * self.a + 2 * self.b
    
    def getP(self):
        return self.a * self.b

    def str(self):
        return "Pravougaonik (a=" + str(self.a) + ", b=" + str(self.b) + ")"
        