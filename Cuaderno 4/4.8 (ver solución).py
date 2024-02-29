'''
Crear una función que compruebe si dos cadenas de caracteres son iguales, sin 
comparar las cadenas completas y sin usar el operador in. 
'''

lista1 = "Hola que tal estás"
lista2 = "Hola que tal estás"
pos = 0

if len(lista1) == len(lista2):
    while lista1[pos] == lista2[pos] and (pos+1) < len(lista1):
        pos += 1 
    print()
    if lista1[pos] == lista2[pos]:
        print("Son iguales")
    else:
        print("No son iguales")
else:
    print("No son iguales")
    

print(len(lista1))
print(pos)