'''
Programar un algoritmo recursivo que obtenga la suma de las edades de todos 
los elementos de una lista de alumnos. Un alumno está caracterizado por tres 
atributos (nombre, edad, titulacion).
'''

alumnos = {}
alumnos["nombre"] = "Alberto", "Samuel", "David"
alumnos["edad"] = 18, 30, 66
alumnos["titulacion"] = "GII", "DGMII", "GIC"

def suma_edades(alumnos, posini, posfin):
    if len(alumnos["edad"]) == 1:
        resultado = alumnos["edad"][0] 
    elif posini == posfin:
        resultado = alumnos["edad"][posini]
    else:
        resultado = alumnos["edad"][posini] + suma_edades(alumnos, posini+1, posfin)
    return resultado

print(suma_edades(alumnos, 0, len(alumnos)-1))

'''
0 != 2
resultado = 20 + suma_edades(alumnos, 1, 2)
1 != 2
resultado = 22 + suma_edades(alumnos, 2, 2)
2 == 2
resultado = alumnos["edad"][posini] = 24

resultado = 20 + 22 + 24 = 66
'''
        