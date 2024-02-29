#Burbuja

lista = [2, 0, 8, 1, 9]
def burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
    return lista

print(burbuja(lista))

#Selección directa (Se busca el hueco, se coge el hueco y luego metemos ahí el elemento menor)
lista = [2, 0, 8, 1, 9]

def selección_directa(lista):
    for inicio in range(len(lista)):
        pos_menor = inicio
        for i in range(inicio+1, len(lista)):
            if lista[i] < lista[pos_menor]:
                pos_menor = i
        lista[inicio], lista[pos_menor] = lista[pos_menor], lista[inicio]
    return lista

print(selección_directa(lista))       

lista = [2, 0, 8, 1, 9]
#Inserción directa (Coger el elemento y ponerlo)
def insercion(lista):
    '''
    '''
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i-1
        while j>=0 and clave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave
    return lista

print(insercion(lista))


def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave
    return lista

def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j>=0 and clave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave
    return lista
































