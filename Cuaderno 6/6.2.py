'''
Realiza un programa que almacene 10 frases diferentes en una lista y nos 
permita ordenar la misma de forma descendentemente utilizando como 
criterio la longitud de la frase. Utiliza el método de inserción directa.
'''

lista = []
for i in range(10):
    frase = input("Introduce una frase")
    lista.append(frase)
    
def ordenar_frases(lista):
    for inicio in range(len(lista)):
        pos_menor = inicio
        for i in range(inicio+1, len(lista)):
            if len(lista[i]) > len(lista[pos_menor]):
                pos_menor = i
        lista[inicio], lista[pos_menor] = lista[pos_menor], lista[inicio]
    return lista

print(ordenar_frases(lista))

