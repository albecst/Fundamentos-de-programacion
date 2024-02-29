# Nombre
nombre = input("Buenas, ¿con quién hablo? ")
print("Encantado", nombre) 
nombre_completo = input("¿Cómo es tu nombre completo? ")
print("Es un nombre estupendo, es un placer", nombre_completo)

MIN_EMPLEADOS = 10 
MIN_FACTURACION = 2 # MEuros
MIN_BALANCE = 2 # MEuros

empleados = 20
facturacion = 18
balance = 5 

es_microempresa_si = empleados < MIN_EMPLEADOS and facturacion <= MIN_FACTURACION or balance <= MIN_BALANCE
print(es_microempresa_si)

#Comprobar que es tipo Booleano
print(type(es_microempresa_si))

print(type(10>2))