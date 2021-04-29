'''
Created on Oct 20, 2018

@author: Marko
'''
import zad1.Krug as krug
import zad1.Pravougaonik as pr

if __name__ == '__main__':
    k = krug.Krug(6)
    p = pr.Pravougaonik(1.1, 2.2)
    
    print(k.str())
    print("Obim je: ", str(k.getO()))
    print("Povrsina je: ", str(k.getP()))
    
    print(p.str())
    print("Obim je: ", str(round(p.getO(), 1)))
    print("Povrsina je: ", str(round(p.getP(), 4)))
    
