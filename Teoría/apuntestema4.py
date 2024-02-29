#ESTRUCTURAS DE DATOS
'''
Arrays: Es una colección de tamaño fijo, a la que se puede acceder por posición. Sus elementos son TODOS del mismo tipo.
Cadenas: Tamaño variable. Array unidimensional cuyo elemento es un carácter.
Registros: Varios tipos de elementos distintos. Se accede por nombre de campo.
Pilas/Colas: colecciones donde lo más importante es el orden de entrada y salida de los elementos. En las pilas, el último en entrar es el primero en salir. (LIFO) En las colas, el primero es el que sale (FIFO).
Lista: se accede por posicion mediante un índice entero.
Conjunto: agrupacion no rdenada de elementos únicos.
Diccionarios: collecion formada por pares claves-valor en la que se accede por clave. Ej. Nombre = Pepe, Apellido = Castillo
Archivo: almacenamiento EXTERNO que puede tener datos iguales o diferentes.
'''

'''
En Python las colecciones son heterogéneas (elementos distintos).
'''

'''
MUTABILIDAD
Son mutables los tipos de datos cuyo valor pueden cambiar una vez creado. EJ= Listas, diccionarios.
Son inmutables los que no pueden cambiar. EJ = números, cadenas y tuplas.
'''

'''
LISTAS
Conjunto de elementos entre corchetes []
Se pueden añadir y quitar elementos.
listaN.append() añade un elemento en la lista
'''

lista = []
for i in range (0, 11):
    lista.append(i)
lista[2]=0 #En la posicion 2 aparece un 0
print(lista)

lista = lista + [50] #Añade el 50 a la lista
print(lista)

lista2 = lista
print(lista2)

lista3 = lista2 + lista #Crea una lista con los elementos de las otras 2, no se suman los elementos. Si lista2 tiene 10 elementos y lista tiene 10, aparecen 20 elementos.
print(lista3)

lista4 = lista[0:2] #Coges los datos de la lista en la posicion 0 y 1 (rango 0, 2)
print(lista4)

del lista[0] #Para eliminar el elemento [x] de la lista
print(lista)

lista.insert(1, 233) #Añade el 233 en la posicion 1. El que estaba en la posicion 1 pasa a la posicion 2.
print(lista)

lista5 = lista*4 #nº elementos*4
print(lista5)

#lista.pop() elimina el último elemento de la lista


'''
SLICING
Forma de obtener susecuencias a partir de secuencias existentes.
secuencia [x:y]
También puede ser secuencia [4:] que va de la posicion 4 al final.
'''

'''
TUPLAS
Conjunto inmutable y ordenado de elementos
Se encierran los elementos entre paréntesis.
'''
tupla = (0.056, 12, 1249.323, 249)
print(tupla)
print(tupla[0])
# a[0] = 1 DA ERROR >:(

#Las tuplas pueden convertirse en listas, y al revés.
print(list(tupla))

tupla = tupla + (60,)
print(tupla)

'''
STRINGS

'''
cadena = "hola" + " " + "mundo"
cadena2 = "Hola"*6

pos = cadena.find("m")
print(pos)

a = cadena.replace("a", "4")
print(a)

split = cadena.split(" ")
print(split)
split2 = cadena.split("m")
print(split2)

lista = list(cadena)
print(lista)

cap = cadena.capitalize()
print(cap)

yeye = cadena.upper()
print(yeye)


'''
DICCIONARIOS
Estructura de datos sin orden entre los elementos.
Se accede mediante una clave que se asocia a cada valor.
Ej: la ficha de un alumno. Para sacar el DNI la clave sería DNI.
'''
diccionario1 = {"Primero": 1, "Segundo":2, "Tercero":3}
print(diccionario1)

print("Primero" in diccionario1) #Me dice True, existe la clave llamada "Primero"
print(diccionario1["Primero"]) #Se accede por clave, no por posición (como en las tuplas/listas)

print(diccionario1.keys())
print(diccionario1.values())
print(1 in diccionario1.values())
print("fosjk" in diccionario1.keys())

diccionario1.update({"Cuarto": 4, "Cuarto":5})
diccionario1["Cuarto"]=6
print(diccionario1)

valor = diccionario1.pop("Cuarto") #Deletear un elemento
del(diccionario1["Tercero"])
print(diccionario1)

#Recorrer el diccionario
diccionario1 = {"Primero":1, "Segundo":2, "Tercero":3, "Cuarto":4}
for clave in diccionario1.keys():
    print(f"{clave}", end = " // ")
print()
    
for values in diccionario1.values():
    print(values, end = " // ")
print()

persona = {"DNI":"01234567A", "Nombre":"Pepe", "Apellido":"Castillo", "Grado":"Ingeniería Informática"}
print(persona)
print(persona["DNI"])

def point(x,y):
    '''
    float, float --> dict
    OBJ:
    '''
    return {"x":x, "y":y}

def triangulo(p1, p2, p3):
    '''
    dict, dict, dict --> dict
    '''
    return{"P1":p1, "P2":p2, "P3":p3}

p1 = point(1.0, 2.0)
print(p1)
p2 = point(3.0, 5.0)
print(p2)
p3 = point(4.0, 2.0)
print(p3)

triangulo = triangulo(p1,p2,p3)
print(triangulo)
print(triangulo.values())
print(triangulo.keys())

#Crear lista con diccionarios
lista_points=[p1,p2,p3]
print(lista_points)
print(lista_points[0])
print(p1["x"])
print(triangulo["P1"]["y"])

p6 = point(1.0, 2.0)
print(p1)
p4 = point(3.0, 5.0)
print(p2)
p5 = point(4.0, 2.0)
print(p3)

print()
print()
print()
print()
print()
'''
En Python podemos representar una matriz con varias listas.
Ej: 
matriz = [[0, 1, 2]
          [2, 4, -1]
          [-3, 0, 2]]
'''

matriz = [[0, 1, 2], 
          [3, 4, 5],
          [6, 7, 8]]

print(matriz[0][2]) #Lista pos 0, elemento pos 2 (0, 1, 2)

def busca_menor(matriz):
    menor = matriz[0][0]
    
    
def factorial(n):
    if n == 1:
        resultado = 1
    if n != 1:
        resultado = n * factorial(n-1)
    return resultado

print(factorial(5))