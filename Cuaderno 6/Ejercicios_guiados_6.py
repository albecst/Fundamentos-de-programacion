'''
Realice un procedimiento que reciba una lista de números reales y lo ordene completo 
(todos sus elementos) de forma ascendente empleando el método de la burbuja.
'''

lista = [8, 5, 0]

def burbuja(lista):
    """ lista -> None
    OBJ: Ordena la lista ascendentemente, método burbuja
    """
    for i in range(len(lista)-1):
        for j in range(len(lista)-1, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
    return lista

print(burbuja(lista))
                
'''
for j in range(2, 0, -1)

j = 2
if lista[2] < lista[1] : 3 < 8
3, 8

j = 1
if lista[1] < lista[0]: 5 < 3
3, 5
'''

'''
Implemente el método de la burbuja para el mismo caso anterior (lista de reales) pero 
esta vez con ordenación descendente y permitiendo ordenación parcial entre dos 
posiciones inicial y final.
'''

lista = [8, 0, 5, 2, 4, 10, 21]

def burbuja2(lista, posini, posfin):
    '''
    '''
    for i in range(posfin):
        for posini in range(posfin):
            if lista[posini] < lista[posini+1]:
                lista[posini], lista[posini+1] = lista[posini+1], lista[posini]
    return lista

print(burbuja2(lista, 0, len(lista)-1))
'''
if 0 <= 2:
if lista[0] < lista[1] : 8, 0
nada

if 1 <= 2:
if lista[1] < lista[2]: 0 < 5
lista[1], lista[2] = lista[2], lista[1] : 0, 5 = 5, 0

'''