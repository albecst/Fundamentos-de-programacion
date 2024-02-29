
#Jugando con int
x = 6
print(f"El valor es {x}")
print("El valor es", x)

a = int(input("¿Cuál es el valor?\n"))

if a == 6:
    print("Muy bien")
else:
    print("Casi")



'''
#Función suma (y lo que debemos poner)
def suma(a,b,c):
    
    float, float --> float
    OBJ: sumar dos números reales
    PRE: vale cualquier número
    
    a = 10
    return (a + b + c)

c = 10
b = -7
print(suma(a,b,c))
'''
'''
def mayor_edad(edad):
    
    
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
edad = 18
print(mayor_edad(edad))
'''
'''
def apotema (h_pirámide, lado_base):
    ''
    float, float --> float
    OBJ: calcular la apotema de un pirámide mediante su altura y el lado de su base
    PRE: h > 0; l > 0
    ''
    return (pow(pow(h_pirámide, 2) + pow(lado_base, 2 ), 0.5))

def área_total (lado_base, h_pirámide):
    ''
    float, float --> float
    OBJ: calcular Área de la pirámide mediante su h y su base
    PRE: h > 0; l > 0
    ''
    return(lado_base * h_pirámide * 4) #Pirámide con base cuadrada

h_pirámide = float(input("Introduce la base de la pirámide "))
lado_base = float(input("Introduce el lado de la base "))
print(apotema(h_pirámide, lado_base))
print(área_total (lado_base, h_pirámide))

'''
