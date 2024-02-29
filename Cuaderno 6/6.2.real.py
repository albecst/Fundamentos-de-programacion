'''
 Realiza un programa que almacene 10 frases diferentes en una lista y nos 
permita ordenar la misma de forma descendentemente utilizando como 
criterio la longitud de la frase. Utiliza el método de inserción directa.
'''

lista = []
for i in range(3):
    frase = input("Introduce una frase")
    lista.append(frase)
    
def insercion(lista):
    '''
    '''
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i-1
        while j >= 0 and clave > lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave
    return lista

print(insercion(lista))