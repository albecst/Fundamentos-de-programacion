'''
Haz un programa para gestionar las notas de una clase de 20 alumnos de los 
cuales sabemos su nombre y la nota obtenida. El programa debe permitir:
a. Introducir los datos de los alumnos por teclado.
b. Dado un nombre de un alumno, buscarlo y modificar su nota, 
mostrando el resultado por pantalla (empleando búsqueda secuencial).
c. Dado un nombre de un alumno, buscarlo y mostrar la información por 
pantalla empleando búsqueda binaria.
d. Realizar la media de todas las notas.
e. Realizar la media de las notas superiores o iguales a 5.
f. Realizar la ordenación (método de selección) de los alumnos por notas 
en orden descendente y mostrar la nota del alumno con mejor nota. 
g. Utilizando el método de inserción, realizar la ordenación de los alumnos 
por notas en orden ascendente y mostrar la nota del alumno que peor 
nota haya sacado.
'''

# a)
Alumnos = []
cuenta = 0
Está = None


while cuenta != 20:
    a = input("Introduce el nombre del alumno: ")
    b = float(input("Introduce su nota: "))
    cuenta += 1
    Alumno = {"Nombre": a, "Nota": b}
    Alumnos.append(Alumno)
print(Alumnos)

Nombre_a_buscar = input("¿A quién estás buscando? ")
for i in range(len(Alumnos)):
    if Alumnos[i]["Nombre"] == Nombre_a_buscar:
        nueva_nota = float(input("Introduce su nueva nota: "))
        Alumnos[i]["Nota"] = nueva_nota
        Está = True
if Está == None:
    print("Este alumno no está")
print(Alumnos)

# c) 
def búsqueda_binaria(Alumnos, nombre):
    posini = 0
    posfin = len(Alumnos) - 1
    while posini <= posfin:
        mid = (posini + posfin) // 2
        if Alumnos[mid] < nombre:
            posfin = mid - 1
        elif Alumnos[mid] > nombre:
            posini = mid + 1
        else:
            return mid
    return None


# d)
suma = 0
cuenta = 0
for i in range(len(Alumnos)):
    nota = Alumnos[i]["Nota"]
    suma += nota
    cuenta += 1
    
media = suma/cuenta
print(f"La media de las notas de todos estos alumnos es {media}")

# e) Media de notas > 5

suma = 0
cuenta = 0
for i in range(len(Alumnos)):
    nota = Alumnos[i]["Nota"]
    if nota > 5:
        suma += nota
        cuenta += 1

media_superior_a_5 = suma/cuenta
print(f"La media de las notas superiores a 5 es {media_superior_a_5}")

# f) Realizar la ordenación (método de selección) de los alumnos por notas en orden descendente y mostrar la nota del alumno con mejor nota.

def ordenar_seleccion(Alumnos):
    '''
    lista --> None
    OBJ: Ordena ascendentemente una lista con el método de selección.
    '''
    for inicio in range(len(Alumnos)):
        pos_menor = inicio
        for i in range(inicio + 1, len(Alumnos)):
            if Alumnos[i]["Nota"] > Alumnos[pos_menor]["Nota"]:
                pos_menor = i
        Alumnos[inicio], Alumnos[pos_menor] = Alumnos[pos_menor], Alumnos[inicio]
    
    return Alumnos

print(ordenar_seleccion(Alumnos))
print("El alumno con mejor nota es", Alumnos[0]["Nombre"], "con un", Alumnos[0]["Nota"])

# g) Utilizando el método de inserción, realizar la ordenación de los alumnos por notas en orden ascendente y mostrar la nota del alumno que peor nota haya sacado.

def ordenar_insercion(Alumnos):
    '''
    lista --> None
    OBJ: Ordenar las notas en orden ascendente con el método de inserción.
    '''
    for i in range(1, len(Alumnos)):
        clave = Alumnos[i]
        j = i-1
        while j >= 0 and clave["Nota"] < Alumnos[j]["Nota"]:
            Alumnos[j+1] = Alumnos[j]
            j -= 1
        Alumnos[j+1] = clave
    return Alumnos

print(ordenar_insercion(Alumnos))
print("El alumno con peor nota es", Alumnos[0]["Nombre"], "con un", Alumnos[0]["Nota"])