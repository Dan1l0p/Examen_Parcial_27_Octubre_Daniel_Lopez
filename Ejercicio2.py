lista = [18, 50, 210, 80, 145, 333, 70, 30]

import sys

def multiplo(lista):
    aa=[]

    for i in range (lista):
        if (i < 200) and (i%10 == int):
            aa.append(i)
            
        if i > 300:
        sys.exit()
    return aa