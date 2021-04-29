'''
Created on Oct 20, 2018

@author: Marko
'''
import zad3.Valjak as valjak

if __name__ == '__main__':
    v = valjak.Valjak(2, 4)
    
    print(v.str())
    print("Povrsina je: ", str(v.getP()))
    print("Zapremina je: ", str(v.getV()))
