'''
Programa una función que evalúe si dos fechas, definidas en términos de día, mes y 
año, son iguales. Asume que las fechas se implementan como diccionarios con entradas 
dia, mes y año y que corresponden a fechas válidas.
'''

'''
def fecha(dia, mes, anno):
 """ int, int, int -> dict
 OBJ: Crea un nuevo diccionario de tipo fecha.
 PRE: dia/mes/anno es una fecha válida.
 """
 return {'dia': dia, 'mes': mes, 'anno': anno}

def iguales(fecha1,fecha2):
 """ dict, dict -> bool
 OBJ: Calcula si una fecha es igual a otra.
 PRE: Los diccionarios fecha1 y fecha2 son de tipo fecha.
 """
 return fecha1 == fecha2

fecha1 = fecha(30, 2, 2005)
fecha2 = fecha(30, 2, 2005)

print(iguales(fecha1, fecha2)) 

persona = {"Nombre":"Alberto", "Apellido":"Castillo","DNI":"09126517W"}

print(persona.keys())
print(persona["Nombre"])

print(persona.items())
print(persona)
'''

'''
Hacer un programa que cree un diccionario con personas (nombre-edad) y permita que 
el usuario pregunte si una persona, elegida por él, está o no en el mismo. Al final se 
mostrará un informe con el contenido del diccionario.
'''

Familia_Gañán_Molina = {"Susana":45, "David":18, "Jorge":45, "Ainhoa": 15}
nombre = input("Introduce un nombre: ")

if nombre in Familia_Gañán_Molina:
    print(f"{nombre} sí está en la lista. Su edad es {Familia_Gañán_Molina[nombre]} años")
    print(f"Además de {nombre} los integrantes de esta lista son: ")
    nombre1 = nombre
    for nombre in Familia_Gañán_Molina:
        if nombre != nombre1:
            print(f"{nombre}, de {Familia_Gañán_Molina[nombre]} años")

else:
    print(f"{nombre} no está en la lista")
    print(f"Los integrantes de esta lista son: ")
    for nombre in Familia_Gañán_Molina:
        print(f"{nombre}, de {Familia_Gañán_Molina[nombre]} años")

