'''
Modifica el programa anterior para que ordene en función del número de 
palabras que hay en la frase. Usa ahora el método de selección directa. Pista: 
será útil utilizar la función split()
'''

lista = []
palabras = []
for i in range(5):
    palabra = input("Introduce una frase: ")
    lista.append(palabra)
    
for j in range(len(lista)):
    division = lista[j].split(" ")
    palabras.append(division)
    
print(palabras)

def selección_directa(palabras):
    '''
    lista --> None
    OBJ: ordenar la lista por número de palabras en orden ascendente.
    '''
    for inicio in range(len(palabras)):
        pos_menor = inicio
        for i in range(inicio + 1, len(palabras)):
            if len(palabras[i]) < len(palabras[pos_menor]):
                pos_menor = i
        palabras[inicio], palabras[pos_menor] = palabras[pos_menor], palabras[inicio]
    return palabras

print(selección_directa(palabras))       
        


            