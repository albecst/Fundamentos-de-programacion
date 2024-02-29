'''
Método de la burbuja:
Es un método de intercambio: Ordena intercambiando parejas de elementos
El elemento de menor clave ✭✭flota✮✮.
Se intercambian los elementos para que el menor vaya ✭✭ascendiendo✮✮.

Básicamente, buscamos el número más pequeño. Si el anterior es más grande, se intercambian las posiciones.
Ej: 5 7 0 --> 5 0 7 --> 0 5 7... repitiéndose len(x) veces.
'''

#Ej
lista = [8, 5, 3, 2, 0, 9]

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
Método de Selección Directa:
Selecciona al elemento más pequeño y lo coloca después de los que ya han sido ordenados.
Para evitar que se repita, la ordenación comienza en el segundo elemento a ordenar.
'''
lista = [8, 0, 3]

def ordenar_seleccion(lista):
    '''
    lista --> None
    OBJ: Ordena ascendentemente una lista con el método de selección.
    '''
    for inicio in range(len(lista)):
        pos_menor = inicio
        for i in range(inicio + 1, len(lista)):
            if lista[i] < lista[pos_menor]:
                pos_menor = i
        lista[inicio], lista[pos_menor] = lista[pos_menor], lista[inicio]
    
    return lista

print(ordenar_seleccion(lista))

'''
Método de inserción directa

'''
def insercion(lista):
    '''
    lista --> None
    OBJ: Ordena ascendentemente una lista mediante el método de inserción.
    '''
    for i in range(1, len(lista)):
        clave = lista[i]
        #Quiero mover elementos de la zona A[0... i-1], mayores que la clave
        #una posicion mas a la derecha
        j = i-1
        while j >= 0 and clave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        
        lista[j+1] = clave