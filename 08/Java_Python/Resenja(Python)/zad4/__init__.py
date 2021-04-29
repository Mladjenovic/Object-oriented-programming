'''
Created on Oct 20, 2018

@author: Marko
'''

import zad4.PP3Prizma as prizma

if __name__ == '__main__':
    p = prizma.PP3Prizma(2, 4)
    
    print(p.str())
    
    print("Povrsina je: ", str(p.getP()))
    print("Zapremina je: ", str(p.getV()))
