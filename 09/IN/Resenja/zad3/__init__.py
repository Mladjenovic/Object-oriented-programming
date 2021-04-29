# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:14:54 2018

@author: Marko
"""

from cddisk import CDDisk
from xcd_storage import XCDStorage
from xcd_storage_dict import XCDStorageDict


def testirajCDDisk():
    print("\n****************** Testiranje klase CDDisk ******************\n")
    d1 = CDDisk(1, "Novi disk", "Pevac hitova")
    d2 = CDDisk(2, "Hitovi", "Pevac")
    print(d1)
    print(d2)
    

def testirajXCDStorage():
    print("\n****************** Testiranje klase XCDStorage ******************\n")
    cds = XCDStorage()
    print(cds)
    
    d1 = CDDisk(1, "Novi disk", "Pevac hitova")
    d2 = CDDisk(2, "Hitovi", "Pevac")
    d3 = CDDisk()
    print(cds.add(d1))
    print(cds.add(d2))
    print(cds.add(d3))
    print(cds.add(d1))
    print(cds)
    
    nadjen = cds.find(1)
    if nadjen != None:
        print("Nadjen disk: " + str(nadjen)) #veoma vazno: konvertovati objekat u string, jer nismo preklopili +
    
    uklonjen = cds.remove(2)
    if uklonjen != None:
        print("Uklonjen disk: " + str(uklonjen)) #veoma vazno: konvertovati objekat u string, jer nismo preklopili +
    
    print(cds.find(5))
    print(cds.remove(5))
    print(cds.remove(1))
    print(cds)
    
    print(cds.add(d1))
    print(cds.add(d2))
    print(cds.add(d3))
    print(cds.add(d1))
    print(cds)
    cds.clear()
    print(cds)


def testirajXCDStorageDict():
    print("\n****************** Testiranje klase XCDStorageDict ******************\n")
    cds = XCDStorageDict()
    print(cds)
    
    d1 = CDDisk(1, "Novi disk", "Pevac hitova")
    d2 = CDDisk(2, "Hitovi", "Pevac")
    d3 = CDDisk()
    print(cds.add(d1))
    print(cds.add(d2))
    print(cds.add(d3))
    print(cds.add(d1))
    print(cds)
    
    nadjen = cds.find(1)
    if nadjen != None:
        print("Nadjen disk: " + str(nadjen)) #veoma vazno: konvertovati objekat u string, jer nismo preklopili +
    
    uklonjen = cds.remove(2)
    if uklonjen != None:
        print("Uklonjen disk: " + str(uklonjen)) #veoma vazno: konvertovati objekat u string, jer nismo preklopili +
    
    print(cds.find(5))
    print(cds.remove(5))
    print(cds.remove(1))
    print(cds)
    
    print(cds.add(d1))
    print(cds.add(d2))
    print(cds.add(d3))
    print(cds.add(d1))
    print(cds)
    cds.clear()
    print(cds)
        
if __name__ == '__main__':
    testirajCDDisk()
    testirajXCDStorage()
    testirajXCDStorageDict()