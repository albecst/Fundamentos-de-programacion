'''
Implemente una función que indique si una palabra contiene las cinco vocales: 
por ejemplo “murciélago”. Modifique posteriormente la función para que detecte 
sólo aquellas palabras que contienen una única vez cada vocal. 
'''

palabra = "murcielago"
lista_cuenta = [0]*5
vocales = ["a", "e", "i", "o", "u"]
recuento_vocales = []

def cinco_vocales(palabra):
    '''
    str -> bool
    OBJ:
    '''
    vocales = ["a", "e", "i", "o", "u"]
    
    for i in range(len(palabra)):
        for j in range (len(vocales)):
            if palabra[i] == vocales [j] and vocales [j] not in recuento_vocales:
                recuento_vocales.append(vocales[j])
    return 5 == len(recuento_vocales)
    
print(cinco_vocales(palabra))
print(recuento_vocales)
