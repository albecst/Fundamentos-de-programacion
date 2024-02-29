'''
3. Una lista de enteros original debe utilizarse para generar dos listas, una con los 
números pares de la original ordenados ascendentemente y otra con los impares 
ordenados descendentemente. La generación de las 2 listas debe hacerse a
medida que se recorre la original, es decir, se toma un número de la original, se 
decide a qué lista (pares o impares) debe ir, y se inserta ordenado en la misma 
de acuerdo con el criterio de la lista (ascendente o descendente). 
'''

lista_enteros = [1,5,6,2,8,4,0,9,111]
lista_pares = []
lista_impares = []

for i in range(len(lista_enteros)):
    if lista_enteros[i] % 2 == 0:
        lista_pares.append(lista_enteros[i])
    if lista_enteros[i] % 2 == 1:
        lista_impares += [lista_enteros[i]]

lista_pares.sort()
print(lista_pares)

lista_impares.reverse()
print(lista_impares)

