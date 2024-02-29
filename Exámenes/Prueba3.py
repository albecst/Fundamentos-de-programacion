'''
m = 10
print(10, end = " ")
miprocedimiento(6, 4)
print(10, end= " ")

m = 6
print(6, end =" ")
mi_procedimiento(2, 4)
print(6, end = " ")

m=2
print(2, end = " ")
mi_procedimiento(-2, 4)
print(2, end=" ")

print(-2)
'''

#10, 6, 2, -2, 2, 6, 10

def modifica (tupla, valor, pos):
    return tupla[0:pos] + (valor,) + tupla[pos+1:]


print(modifica((1,2,3,4), 20, 1))

tupla = (20, 2, 11, 5, 3)
for i in range(1, len(tupla)):
    for j in range(len(tupla) -i):
        if tupla[j] > tupla[j+1]:
            aux =  tupla[j]
            tupla = modifica(tupla, tupla[j+1], j)
            tupla = modifica(tupla, aux,  j+1)

print(tupla)


alimentos = {"Sabio":[1000, 2000, 3000], "Gruñón": [4000], "Mocoso": [5000, 6000], "Mudito": [7000, 8000, 9000]}

def ganador(alimentos):
    nombre = None
    mayor = 0
    suma = 0
    for k in alimentos:
        for calorias in alimentos[k]:
            suma += calorias
            if suma > mayor:
                nombre = k
                mayor = suma
        suma = 0
    return nombre, mayor

print(ganador(alimentos))

def funcion_misteriosa(mi_lista):
    a = []
    for elemento in mi_lista:
        if type(elemento) == list:
            a += funcion_misteriosa(elemento)
        else:
            a += elemento
    return a

print(funcion_misteriosa(["a", ["b", ["c", ["d"]], "e"], "f"]))

'''
["a", lista1, "f"]
lista1 = ["b", lista2, "e"]
lista2 = ["c", lista3]
lista3 = ["d"]

a = []
a = ["a", ]

elemento == lista1
a += funcion_misteriosa(lista1)
a += "f"

funciona_misteriosa(lista1):
    a += "b"
    a += funcion_misteriosa(lista2)
    a += "e"
    
funciona_misteriosa(lista2):
    a += "c"
    a += funcion_misteriosa(lista3)
    
fucion_misteriosa(lista3)
    a += "d"
    
a = ["a", "b", "c", "d", "e", "f"]
'''

# Generar una lista con tantas tuplas como elementos haya en lista_b

lista_b = [6, 4, 6, 1, 2, 2]
mi_lista = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
resultado = []
for i in lista_b:
    resultado.append((i, mi_lista.index(i)))
    
print(resultado)

#[(6,2), (4,8), (6,2), (1,3), (2,7), (2,7)]


def otro_misterio(mi_lista, cuanto):
    for i in range(len(mi_lista)):
        mi_lista[0][i] += cuanto
    print(mi_lista[0])
    
sublista = [1, 2, 3, 4, 5]
mi_lista = []
for i in range(5):
    mi_lista.append(sublista)
print(len(mi_lista))
otro_misterio(mi_lista, 3)
print(mi_lista)

#mi_lista=[5 veces la sublista] = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

#De la primera lista
#mi_lista = [[4, 5, 6, 7, 8]]
#Tooooooooooooooda la lista xd lol

