'''
for amiga in ["Marta", "Elsa", "Ana", "Andrea"]:
    invitacion = amiga + ", te espero en mi fiesta."
    print(invitacion)
'''
'''
for i in range (7, 20): #Desde el 7 hasta 20-1
    print(i, end=" ")
    
words = ["cat", "dog", "lion"]
for w in words:
    print(w, end= ""/"")
'''
'''
x = 0
for i in range (1,20,2): #Del 1 al 20-1, de 2 en 2
    x = x + i
print(x)

1 = 0 + 1
4 = 1 + 3
9  = 4 + 5
16  = 9 + 7
25   = 16 + 9
'''

'''
for i in range (0, 100, 10):
    print(i, end=" ")
'''    

'''
x = 0
import random
for i in range(10):
    i = random.randint(0,100)
    x = x + i
print(x)
'''

#El factorial de 3 = 3*2*1
'''
def factorial(n):
    x = 1
    for i in range (1, n+1):
        x = x * i
    return x

print(factorial(4))  
'''

#1 = 1*1
#2 = 1*2  
#6 = 2*3
#Deuelve result = 6

'''
for i in range (2, 11, 2): #2, 4, 8, 10
    for j in range(1,11):
        print(i, "*", j, "=", i*j)
    print("-------------")
'''
'''
for j in range(1,11,2):
    for i in range(1,11):
        print(j, "*", i, "=", j*i)
    print("-------")
'''    

'''
n = 5
for i in range(2, n+1): #2,3,4,5
    x = 1
    print(1, end=" ")
    for j in range (2, i): #2; 2,3; 2,3,4
        x = x + j
        print(" + ", j, end=" ")
    print(" = ", x)
'''

#1+0 = 1
#1+2 = 3
#1+2+3 = 6
#1+2+3+6 = 10

#WHILE
#while (condicion):
   #sentencia(s)
   
'''
n=10
while (n>0):
    print(n)
    n = n+1
'''

'''
n=10
while (n>0):
    print(n)
    n = n-1
print("Despegueeee")
'''

'''
import random
inverso = 0
n = 79
print(f"Numero a invertir: {n}")

while(n>0):
    inverso = inverso*10
    inverso = inverso + n%10 #9
    n = n//10 #7

print(inverso)
'''
'''

#Contador
def contar_digitos(n):
    contador = 0
    while(n>0):
        contador = contador + 1
        n = n//10
    return(contador)
print(contar_digitos(154))

#154//10 = 15 (contador = 0 + 1)
#15//10 = 1 (contador = 1 + 1)
#1//10 = 0 (contador = 1 + 1 + 1)
'''
'''
def invertir(n):
    inverso = 0
    while (n>0):
        cifra = n % 10
        inverso = inverso*10 + cifra
        n = n//10
    return inverso

print(invertir(71))
'''
'''
import random
valor = random.randint(0,100)

def media(valor):
    N = 0
    suma = 0
    while(valor != 0):
        suma = suma + valor
        N = N + 1
        return(suma/N)
        
print(media(valor))
'''
'''
import random
CENTINELA = 0
cuantos = 0
suma = 0
valor = random . randint (0 ,100) # iteracion pre - bucle
while ( valor != CENTINELA ) :
    suma += valor
    cuantos += 1
    valor = random . randint (0 ,100)
if ( cuantos >0) :
    print ("La media es: ", suma / cuantos )
'''