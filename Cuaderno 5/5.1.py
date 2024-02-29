'''
Programar un procedimiento recursivo que compruebe si un cierto número se 
encuentra o no en una lista
'''
'''
n = 4
lista = [1, 2, 5, 3, 4]
Si posini == posfin != n:
    return False
    
n = 4
búsqueda(4, 0, 4, lista)
posini != posfin
búsqueda(n, 1, 4, lista)
lista[1] != 4

'''
lista = [1, 2, 5, 3, 4]
def búsqueda(n, posini, posfin, lista):
    '''
    int, int, int, lista -> str
    OBJ: ver mediante recursión si un número pertenece a una lista.
    '''    
    if posini == posfin:
        if lista[posini] == n:
            print("Sí está")
        if lista[posfin] != n:
            print("No está")
        
    if posini < posfin:
        if lista[posini] == n:
            print("Sí está")
        else:
            búsqueda(n, posini+1, posfin, lista)
        return
print(búsqueda(3, 0, len(lista)-1, lista))
