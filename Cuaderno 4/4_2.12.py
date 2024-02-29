'''
Programa una función que reciba un diccionario y una lista y que como salida genere 
dos listas: una con todos los valores de aquellos elementos de la lista que están en el
diccionario, y otra con los que NO están en el diccionario
'''

diccionario = {"valor1":1, "valor2":2}
diccionario["valor3"] = 3
lista = [1,2,3,4,5]

listarepe = []
listanorepe = []

for i in range(len(lista)):
    if lista[i] in diccionario.values():
        listarepe.append(lista[i])
    else:
        listanorepe.append(lista[i])

print(listarepe)
print(listanorepe)
print(diccionario)