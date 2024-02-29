'''
Si tenemos un diccionario que contiene como claves el nombre de una persona y como 
valor una lista con sus “preferencias personales”, es posible programar una función 
agregaPreferencia(diccionario, persona, preferencia) tal que: 
a. Si la persona no existe, la agrega al diccionario con una lista que contiene un 
solo elemento que es la nueva preferencia. 
b. Si la persona existe y la preferencia actual existe en su lista, no tiene ningún 
efecto, pero si dicha preferencia no existe en su lista, la agrega a la lista.
'''
preferencia = ["Futbol"]
persona = "Antonio"
diccionario = {persona: preferencia}


def agregaPreferencia(diccionario, persona, preferencia):
    '''
    dict, str, list -> dict
    '''
    x = input("Introduce el nombre de la persona: ")
    y = input("Introduce su preferencia: ")    
    lista = []
    lista.append(y)
    if x in diccionario.keys():
        if y != diccionario[persona]:
            diccionario[x] += lista
    if x not in diccionario.keys():
        diccionario[x] = lista
    return diccionario

print(agregaPreferencia(diccionario, persona, preferencia))
