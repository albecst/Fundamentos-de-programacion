lista = [3, 2, 6, 0, 4, 1]
'''
Empieza en el 3
3 no es mayor que 5
3 es menor que 2, se guarda el 2.
2 no es mayor que 9
0 es menor que 2, se guarda el 0.
Intercambiamos el 0 con el 3.

Ahora empezamos desde el 5
'''
def select_sort(lista):
    for i in range(len(lista)): #0
        posición_menor = i #0
        for j in range(i+1, len(lista)):
            if lista[j] < lista[posición_menor]:
                posición_menor = j
        lista[i], lista[posición_menor] = lista[posición_menor], lista[i]
    return lista
        

print(select_sort(lista))





































lista = [3, 2, 6, 0, 4, 1]

def papapa(lista):
    '''
    '''
    for i in range(len(lista)):
        pos_menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i], lista[pos_menor] = lista[pos_menor], lista[i] 
    return lista

print(papapa(lista))

'''
i = 0
pos_menor = 0
'''

