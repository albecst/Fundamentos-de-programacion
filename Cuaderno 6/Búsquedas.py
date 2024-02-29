'''
BÚSQUEDA SECUENCIAL
La de toda la vida, haces un bucle while y cuando lo encuentra para.
'''

'''
BÚSQUEDA BINARIA
Va dividiendo la lista en 2 hasta que encuentre algo.
La lista tiene que estar ordenada.
'''
lista = [1, 2, 3, 4, 5]
def busqueda_binaria(lista, n):
    pos = None
    posini = 0
    posfin = len(lista)
    while posini <= posfin and pos == None:
        centro = (posini+posfin)//2
        if n == lista[centro]:
            pos = centro
        elif n < lista[centro]:
            posfin = centro-1
        else:
            posini = centro+1
    return pos

print(busqueda_binaria(lista, 5))