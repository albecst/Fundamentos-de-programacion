
'''
import random
n = random.randint(0,100)
print(n)
if n % 2 == 0:
    print("Par")
else:
    print("Impar")
'''
'''
n = float(input("Introduce un número:\n"))
if n % 2 == 0:
    print("Es par")
else:
    print("Es impar")
    
if n > 50:
    print("Además, es mayor a 50")
elif n < 50:
    print("Además, es menor a 50")
elif n == 50:
    print("Es 50")
'''

'''
import random
día = random.randint(1,7)

if día == 1:
    print("Es lunes")
elif día == 2:
    print("Es martes")
elif día == 3:
    print("Es miércoles")
elif día == 4:
    print("Es jueves")
elif día == 5:
    print("Es viernes")
elif día == 6:
    print("Es sábado")
elif día == 7:
    print("Es domingo")

if día > 5:
    print("Es fin de semana")
else:
    print("Es entre semana")
'''

'''
horas = float(input("Introduce el número de horas trabajadas:\n"))
dinero = 20 #€/h
sueldo = horas*dinero

if horas < 40:
    print(f"{sueldo} euros" )
else:
    print(f"{sueldo*1.5} euros")
'''

'''
año = 2023
x = input("¿Cuándo naciste? \n")

try:
    año_nacimiento = int(x)
except:
    print("Estás metiendo texto en vez de un número, subnormal :) >:( ")
    
else:
    edad = año - año_nacimiento
    print(edad)
'''

'''
n1 = float(input("Introduce el primer número"))
n2 = float(input("Introduce el segundo número"))
'''
'''
txt = "Hola"
print(txt[2])
'''

'''
vocal = ["a", "e", "i", "o", "u"]
for letra in "Universidad de Alcalá":
    if vocal(letra):
        print(letra, end = '')
    else:
        print("#", end= '')

'''

'''
for n in range(5):
    print(f"El valor de n es {n}")
'''

'''
x = 0
for i in range (1, 20, 2):
    x += i # x = x + i
    print(x)
'''

#VIVAN GAUSS Y LEÓN
suma = 0 #Comienza en 0
for i in range (101):
    suma = suma + i #x = x+i
    print(suma)


