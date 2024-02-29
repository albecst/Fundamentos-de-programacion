'''
Implementar una función que pone en mayúsculas la primera letra de cada una 
de las palabras de una frase, sin usar el método title(). 
'''
frase = "hola que tal estás yo muy bien y tú"
frase_s = frase.split( )
print(frase_s)
print(frase_s[0])


def mayúscula(frase):
    '''
    Str -> Str
    
    '''
    frase_s = frase.split( )
    for i in range(len(frase_s)):
        palabra = frase_s[i]
        Palabra = palabra.capitalize()
        print(Palabra, end = " ")
    return " "

print(mayúscula(frase))

'''
"Cristina" (clave) --> [0, 0, 0] (Valor)
'''