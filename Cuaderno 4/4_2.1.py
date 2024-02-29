'''
Piensa en las estructuras de datos que permitan almacenar información sobre personas 
con objeto de hacer un estudio estadístico. Así, se deberá almacenar el nombre, sexo y 
edad de cada persona. Programa posteriormente una función para leer por teclado 
datos relativos a una persona y otra que muestra dichos datos por pantalla.
'''

Persona0 = {"Sexo":"H", "Edad": 23, "Nombre": "Juan"}
Persona1 = {"Sexo": "M", "Edad": 33, "Nombre": "Rosario"}
Persona2 = {"Sexo": "H", "Edad": 19, "Nombre": "Pepe"}
Total = [Persona0, Persona1, Persona2]

persona = input("¿De qué persona quieres saber información? (Introduce un número del 0 al 2)")

def info2(Total):
    '''
    '''
    for i in range(len(Total)-1):
        if Total[i]["Nombre"] == persona:
            print(Total[i])
    return " "

print(info2(Total))
