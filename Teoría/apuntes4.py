#Las listas se indican con []
#Las tuplas con ()
#los diccionarios con {}
'''
milista1 = [1,2,3,4,"hola",True]
mitupla1 = (1,2,3,4,"hola",True)

unaLista = [1,2,3]
[a,b,c] = unaLista

print(a,b,c)
print(unaLista[1])

diccionario = {}

diccionario["nombre"] = "Antonio", "Sofía"
diccionario["apellido"] = "García"
diccionario["edad"] = 33

print(diccionario["edad"])
print(f"{diccionario}")
'''

#Para ver letras
mi_cadena = "Hola a todos"
print(mi_cadena[0])

#Para separar las palabras
tokens = mi_cadena.split("a") #Lo que hay dentro del paréntesis es el separador
tokens = mi_cadena.split() #Lo que hay dentro del paréntesis es el separador
print(tokens)

lista_1 = [1,3,6,9,2,87,34]

print(lista_1.sort()) #Ordena mi lista
print(reversed(lista_1))

# en lista.index(Antonio) me dice qué posición tiene el nombre Antonio (al contrario que usar corchetes)