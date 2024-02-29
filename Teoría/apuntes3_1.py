'''
import random
n = random.randint(0,100)

if n % 2 == 0:
    print(f"{n} es par")
else:
    print(f"{n} es impar")
'''    
'''
def dinero(horas_trabajadas):
    ''
    float, float --> float
    OBJ:
    PRE:
    ''
    sueldo = 20 # €/h
    if horas_trabajadas <= 40:
        sueldo = horas_trabajadas*20
        print(f"{sueldo} euros")
    if horas_trabajadas > 40:
        sueldo = horas_trabajadas*sueldo + (horas_trabajadas-40)*1.5
        print(f"{sueldo} euros")
    

print(dinero(40))
'''

año_actual = 2023
x = input("Introduce el año en el que nació: ")
try:
    año_nacimiento = int(x)
except:
    print("Algo ha fallado. ¿Estás metiendo texto?")
else:
    edad = año_actual - año_nacimiento
    print("Tu edad es", edad ,"años")
    