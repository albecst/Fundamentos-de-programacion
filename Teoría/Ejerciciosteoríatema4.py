'''
CUENTALETRAS
El rpograma tiene que pedir al usuario una letra y cuando ponga un numero que temrine. Dirá cuantas veces has puesto cada letra.
'''
'''
LETRAS = "abcdefghijklmnopqrstuvwxyz"
lista_contadores = [0]*len(LETRAS)
print(lista_contadores)
request = input("Introduce una letra: ")
cuenta = 0

while request in LETRAS:
    for i in range(len(LETRAS)):
        if request == LETRAS[i]:
            lista_contadores[i] = lista_contadores[i] + 1
            cuenta += 1
    request = input("Introduce otra letra: ")

for j in range(len((LETRAS))):
    print(LETRAS[j], lista_contadores[j])
print(f"Has introducido {cuenta} carácteres")

'''
'''
Ejercicio 2
Crear una lista de 10 números aleatorios y hacer:
- Una función que reciba la lista y devuelva el menor.
- Una función que reciba la lista y devuelva el mayor.
- Una función que reciba la lista y un elemento y devuelva si está en la lista.
- Una función que reciba la lista y devuelva la posición del elemento.
'''

import random
lista = []
lista2 = []
for i in range(10):
    numero = random.randint(0, 10)
    lista +=[numero]
    lista2.append(numero) #También se puede hacer así

print(lista)
print(lista2)

def encontrar_mayor(lista):
    mayor = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

print(f"El número mayor de la lista es {encontrar_mayor(lista)}")

def encontrar_menor(lista):
    menor = lista[0]
    for j in range(len(lista)):
        if lista[j] < menor:
            menor = lista[j]
    return menor

print(f"El número menor de la lista es {encontrar_menor(lista)}")

def encontrar_elemento_y_posicion(lista, n):
    pos = 0
    while n != lista[pos] and (pos+1) < len(lista):
        pos += 1
    
    if n == lista[pos]:
        print(f"El número {n} está en la lista, en la posición {pos}")
    if n != lista [pos]:
        print(f"El número {n} no está en la lista")

n = int(input("¿Qué elemento quieres ver si está en la lista?"))
print(encontrar_elemento_y_posicion(lista, n))

def veces_elemento(lista, x):
    pos = 0
    cuenta = 0
    while (pos+1) < len(lista):
        if x == lista[pos]:
            cuenta += 1
        pos += 1
    print(f"Sale el número {x} *{cuenta}* veces")
    
x = int(input("¿Qué elemento quieres ver si está en la lista y cuantas veces sale?"))
print(veces_elemento(lista, x))