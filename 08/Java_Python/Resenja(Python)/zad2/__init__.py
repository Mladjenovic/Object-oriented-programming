'''
Created on Oct 20, 2018

@author: Marko
'''

import zad1.Pravougaonik as pr

    
def najvecaPovrsina(pravougaonici):
    if pravougaonici == None:
            return None;
    pMax = pravougaonici[0]
    
    for p in pravougaonici:
        if p.getP() > pMax.getP():
            pMax = p
    
    return pMax


if __name__ == '__main__':
    
    print("Niz realnih brojeva")
    a = [0.0] * 3
    a[0] = 2.5

    #iteracija kroz niz
    for i in range(len(a)):
        print("Element na poziciji " + str(i) + " je " + str(a[i]))
        

    print("\nNiz celih brojeva")
    
    #kreiranje i inicijalizacija niza
    b = [1, 7, 9, 3, 4]
    
    for i in range(len(b)):
        print("Element na poziciji " + str(i) + " je " + str(b[i]))
    
    
    print("\nNiz objekata")
    pravougaonici = [None] * 5
    pravougaonici[0] = pr.Pravougaonik(10, 2)
    pravougaonici[1] = pr.Pravougaonik(5, 8)
    pravougaonici[2] = pr.Pravougaonik(3, 9)
    pravougaonici[3] = pr.Pravougaonik(7, 1)
    pravougaonici[4] = pr.Pravougaonik(6, 11)
    
    for i in range(len(pravougaonici)):
        print("Pravougaonik na poziciji " + str(i) + " ima povrsinu " + str(pravougaonici[i].getP()))
    
    #pravougaonik sa najveæom površinom
    print()
    pMax = najvecaPovrsina(pravougaonici)
    if pMax != None:
        print("Pravougaonik sa najvecom povrsinom je pravougaonik sa stranicama " + str(pMax.getA()) + " i " + str(pMax.getB()));
