'''
def potenciasDe5 (n): 
    result = 1
    for i in range (0,n+1): 
        print ("5 ^",i, " = ", result)
        result *= 5
    return 
potenciasDe5(23)

n = 5
for i in range(2, n+1):
    print(1, end = "")
    suma = 1
    for j in range (2, i):
        suma = suma + j
        print("+", j, end = " ")
    print( " = ", suma)
'''

'''
import random
n = random.randint(0, 100)
print(n)
b = n // 10
a = n % 10

print(f"{a}{b}")
'''
'''
import random
n = random.randint(0,100)
suma = n
contador = 0
print(n, end=" ")

while n != 0:
    n = random.randint(0, 100)
    contador = contador + 1
    suma = suma + n
    print(n, end = " ")
print()

media = suma / contador
print(suma)
print(media)
print(contador)
'''
'''
dinero = int(input('Introduce la cantidad en €: '))
for actual in [500, 200, 100, 50, 20, 10, 5, 2, 1]:
    num_billetes = dinero // actual
    dinero %= actual
    if (num_billetes > 0):
        if (actual<5):
            print("Monedas de ", actual, " euros: ", num_billetes)
        else:
            print("Billetes de ", actual, " euros: ", num_billetes)
    
'''
'''
def esta_en_diagonal_principal(i,j):
    ''
    ''
    return i == j

print(esta_en_diagonal_principal(3,3))

def esta_en_diagonal_inversa(i,j,n):
    ''
    ''
    return i + j == n

print(esta_en_diagonal_inversa(3,1,4))
'''
'''
def dibujarRombo(filas):
    for i in range(1, filas+1):
        for j in range(filas, i-1, -1):
            print(" ", end="")
        for k in range (1,filas+1):
            print("* ", end="")
        print()
    return

dibujarRombo(6)

def escribeTablaVerdad ():
    """nada --> nada
    OBJ: escribe tabla de verdad de AND"""
    for p in [True, False]:
        for q in [True, False]:
            print(p, q, p and q)
escribeTablaVerdad()
'''

'''
def calcular (a,b):
    a = b % 2
    b = a * a + 3 * b - 6
    a += b*2
    return a,b
x = 6
y = 4
y, x = calcular (x,y)
print ('x = ', x, ' y = ', y)
'''

'''
def f(y,z):
    y = y + 3
    z = z - 1
    print (x,y,z)
def R():
    a = x
    z = a+y
    print (x,y,z)
    r = z
def g(z,u,v):
     if (z % v == u % v):
        f(z,u)
     else:
        z = R()
     print(x,y,z)
#prueba
x = 10
y = 2
z = 1
g(x,y,2*z)
print(x,y,z)
'''

'''
import random
n = random.randint(-1,1000)
def suma_multiplos_17(n):
    ''
    int -> int
    ''
    cuenta = 0
    suma = 0
    while cuenta <= 100:
        cuenta = cuenta + 1
        if n % 17 == 0:
            suma = suma + n
        n = random.randint(-1,1000)
    print()
    return suma

print (suma_multiplos_17(n))
'''


import random
x = random.randint(-1,1)
y = random.randint(-1,1)
print(x, y)

def cuadrante (x,y):
    while x*x + y*y != 1:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        print(x, y)
        if x*x + y*y == 1:
            if x > 0 and y > 0:
                print(1)
            elif x < 0 and y > 0:
                print(2)
            elif x < 0 and y < 0:
                print(3)
            elif x > 0 and y < 0:
                print(4)
            elif x > 0 and y == 0:
                print(1, 4)
            elif x < 0 and y == 0:
                print(2, 3)
            elif x == 0 and y > 0:
                print(1, 2)
            elif x == 0 and y < 0:
                print(3, 4)
            elif x == 0 and y == 0:
                print(1, 2, 3, 4)
    return

print(cuadrante(x, y))


#Número de tiradas necesarias para que salgan 3 seises
'''
import random
n = random.randint(1,6)
print(f"Tirada 1 = {n}")

def tiradas(n):
    tiradas = 1
    while n != 6:
        n = random.randint(1,6)
        tiradas += 1
        print(f"Tirada {tiradas} = {n}")
    print("¡Primer 6!")
    n = random.randint(1,6)
    tiradas += 1
    print(f"Tirada {tiradas} = {n}")
    while n != 6:
        n = random.randint(1,6)
        tiradas += 1
        print(f"Tirada {tiradas} = {n}")
    print("¡Segundo 6!")
    n = random.randint(1,6)
    tiradas += 1
    print(f"Tirada {tiradas} = {n}")
    while n != 6:
        n = random.randint(1,6)
        tiradas += 1
        print(f"Tirada {tiradas} = {n}")
    print("¡Tercer 6!")    
    return tiradas
print(f"Han sido necesarias {tiradas(n)} tiradas")
'''

'''
altura = 10
for i in range(1, altura):
    print("- " * i)
'''

'''
import random
a = random.randint(0, 180)
b = random.randint(0,180)
c = random.randint(0,180)

def tipo_triángulo(a,b,c):
    ''
    float, float, float --> str
    ''
    if a == 90 or b == 90 or c == 90:
        print("Triángulo rectángulo")
    elif a < 90 and b < 90 and c < 90:
        print("Triángulo acutángulo")
    elif a > 90 or b > 90 or c > 90:
        print("Triángulo obtusángulo")
    return

while a + b + c != 180:
    a = random.randint(0, 180)
    b = random.randint(0,180)
    c = random.randint(0,180)
print(a, b, c)

print(tipo_triángulo(a,b,c))
'''
'''
n = 7
m = n//2
for i in range (1, m + 1):
    print("    "*m, end = "")
    print("*")
print("*   " * n)
for j in range (m + 2, n+1):
    print("    "* m, end = "")
    print("*")

'''
'''
n = int(input("Introduce un número"))
suma = 0
numeros = 0
numanterior = 0
mayor = 0
menor = 0
distanciaanterior = 0
while n > numanterior:
    distancia = n - numanterior
    numanterior = n
    suma += n
    numeros += 1
    if distancia > distanciaanterior:
        distanciaanterior = distancia
        print(distanciaanterior)
    
    n = int(input("Ahora, introduce un número mayor que el anterior"))

if numeros <= 2:
    print("Secuencia no válida")
if numeros > 2:
    media = suma/numeros
    print(f"La media de estos números es {media} y la secuencia está formada por {numeros} numeros")

print(mayor, menor, end = "\n")
print(f"La distancia máxima es {distancia}", end="\n")
'''

def procedimiento(m,n):
    while n>0:
        r = n %10
        for k in range (r, 0, -1):
            print(m, end = "")
        print()
        n = n//10
    return "nada"
print(procedimiento("o", 1234321))
    