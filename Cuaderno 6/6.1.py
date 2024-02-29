'''
Implementa un programa que, dado un número finito de fechas, nos permita 
buscar una fecha por año, mes o día, así como la ordenación de las mismas 
por año. Nota: emplea el método de búsqueda binaria.
'''

día = [1, 5, 11, 14, 20]
mes = [1, 5, 8, 9, 10]
año = [2012, 2009, 2006, 2020, 2002]

n = 2006

def buscar_año(año):
    for i in range(len(año)-1):
        for j in range(len(año)-1, 0, -1):
            if año[j] < año[j-1]:
                año[j], año[j-1] = año[j-1], año[j]
    return año

año_nuevo = buscar_año(año)
print(año_nuevo)           


def posicion(año_nuevo, n):
    pos = 0
    posini = 0
    posfin = len(año_nuevo)-1
    while posini <= posfin and pos == 0:
        centro = (posini + posfin) // 2
        if año_nuevo[centro] == n:
            pos = centro
        elif n < año_nuevo[centro]:
            posfin = centro - 1
        else:
            posini = centro + 1
    return pos

print(posicion(año_nuevo, 2009))


def bgfb(lista, n):
    pos = None
    posini = 0
    posfin = len(lista)-1
    while posini < posfin and pos == None:
        centro = (posini + posfin)//2
        if lista[centro] == n:
            pos = centro
        elif n < lista[centro]:
            posfin = centro - 1
        else:
            posini = centro + 1
    return pos