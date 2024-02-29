'''
Crear una lista de enteros, inicializarlos según valores aleatorios en el rango 1..20 
y computar la media de los valores, el valor más alto y el más bajo (todo ello 
utilizando listas).
'''

import random
lista = []
mayor = 0
menor = 19
suma = 0

for i in range(4):
    n = random.randint(1, 20)
    suma += n
    lista.append(n)
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
 

media = suma/len(lista)
print(f"Su lista es {lista}")
print(f"La media de todos estos números es {media}")
print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")