# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:14:54 2018

@author: Marko
"""

from Krug import Krug
from Pravougaonik import Pravougaonik
from Kvadrat import Kvadrat

def ispisiPovrsinu(gf):
    print(gf)
    print("Povrsina je: ", str(gf.getPovrsina()), "\n")
    
if __name__ == '__main__':
    k = Krug(4)
    k2 = Krug(1.5)
    k3 = k + k2
    
    ispisiPovrsinu(k)
    ispisiPovrsinu(k2)
    ispisiPovrsinu(k3)
    
    
    p = Pravougaonik(2, 3)
    p2 = Pravougaonik(1.1, 2.2)
    
    ispisiPovrsinu(p)
    ispisiPovrsinu(p2)
    
    if p == p2:
        print("p i p2 su isti\n")
    else:
        print("p i p2 nisu isti\n")
        
    
    kv = Kvadrat(4)
    kv2 = Kvadrat(1.5)
    
    ispisiPovrsinu(kv)
    ispisiPovrsinu(kv2)
    
    if kv == kv2:
        print("kv i kv2 su isti\n")
    else:
        print("kv i kv2 nisu isti\n")