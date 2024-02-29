'''
En un programa se busca la mayor eficiencia: menor consumo de tiempo, memoria, tiempo de CPU...
La complejidad algorítmica mide la eficiencia de un algoritmo, determinando el número mínimo de operaciones que se realizan.
'''
#Búsqueda secuencial
#Vas una por una recorriendo todo.

#Búsqueda binaria
#Tienen que estar ordenados los elementos. Lo que se hace es dividir la lista en 2, 2, 2, 2... para ser mas rápido.
#El rango lo reduzco a la mitad, y veo si es menor o mayor. Vuelvo a reducir a la mitad...
#EJ:
def posicion(A, elemento):
    '''
    '''
    pos = None
    ini = 0
    fin = len(A) - 1
    while ini <= fin and pos == None:
        centro = (ini + fin)//2
        if lista[centro] == elemento:
            pos = centro
        elif elemento < lista[centro]:
            fin = centro - 1
        else:
            ini = centro + 1
    return pos

lista = [1,2,3,4,5,6,7,8,9]
print(posicion(lista, 3))

#EJ:
def posicion (lista , buscado):
    """
    list , int -> int
    OBJ : Posicion en una lista de clientes , None si no esta .
    PRE : lista ordenada por num_cliente
    """
    pos = None
    ini = 0
    fin = len ( lista ) - 1
    while ( ini <= fin and pos == None):
        centro = (ini + fin ) //2
        if lista [ centro ]["num_cliente"] == buscado : pos = centro
        elif buscado < lista [ centro ]["num_cliente"]: fin = centro -1
        else : ini = centro + 1
    return pos
clientes = [{"nombre":"Angel Perez", "num_cliente": 1}, {"nombre":"Angela Perez", "num_cliente": 2}]

print(posicion(clientes, 1))

'''
Ordenación: ordenas los elementos de mayor a menor. Es menos eficiente, pero más fácil.
'''
#MÉTODO DE LA BURBUJA
def ascender_menor (lista, primero , ultimo ) :
    """ lista , int , int -> None
    OBJ : Encuentra el menor en un rango y lo lleva a la
    primera posicion . Modifica la lista .
"""
    for i in range (ultimo , primero , -1) :
        if (lista[i] < lista[i -1]) :
            lista[i] , lista[i -1] = lista[i -1] , lista[i]
    return lista
    
lista = [4,7,2,1,8,9,10,20,40,23,52,63,334,634,39,46,343,2,54,543,436,245,676,56,7,6,44,444,56,]

for j in range(len(lista)-1):    
    (ascender_menor(lista, 0, len(lista)-1))
    
print(ascender_menor(lista, 0, len(lista)-1))


#Método de selección directa

A = [22, 10, 12, 10, 1, 5]

def ordenar_seleccion (A) :
    """ lista -> None
    OBJ : Ordena ascendentemente una lista .
    Metodo de seleccion . Modifica la lista . """
    
    for inicio_pasada in range (len (A) ) :
        # Encuentra el menor de la parte desordenada
        posicion_menor = inicio_pasada
    for i in range ( inicio_pasada + 1 , len (A) ) :
        if A[i] < A[ posicion_menor ]:
            posicion_menor = i
            # Intercambia el primero con el menor
    A[ inicio_pasada ] , A[ posicion_menor ] = A[ posicion_menor ] , A[ inicio_pasada ]
    return A


print(ordenar_seleccion(A))

#Método de inserción directa


