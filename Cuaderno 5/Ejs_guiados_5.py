'''
Factorial
n! = n*(n-1)!
'''
    
def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    if n > 1:
        resultado = n*factorial(n-1)
    return resultado

print(factorial(4)) 

'''
si n>1:
resultado = 4*factorial(3)
resultado = 3*factorial(2)
resultado = 2*factorial(1)
resultado = 2*1
resultado = 3*factorial(2 (2))
resultado = 4* 3*(factorial(2)
resultado = 24
'''

'''
Problema: Multiplicar dos numeros por sumas sucesivas.
3*3 = 3+3*2 = 3+3+3*1
'''

def sumas_sucesivas(n,m):
    if m == 1:
        resultado = n
    if m > 1:
        resultado = n + sumas_sucesivas(n, m-1)
    return resultado

print(sumas_sucesivas(3,3)) 

'''
Fibonacci
1, 1, 2, 3, 5, 8, 13, 21...
n = 0 = 1
n = 1 = 1
n = 2 = 2
n = 3 = 3
n = 4 = 5; 5 = 2 + 3 = fibonacci(n-2) + fibonacci(n-1)
n = 5 = 8
'''

def Fibonacci(n):
    if n == 0:
        resultado = 1
    if n == 1:
        resultado = 1
    if n >= 2:
        resultado = Fibonacci(n-2) + Fibonacci(n-1)
    return resultado

print(Fibonacci(5))

#Fibonacci(3)
#resultado = Fibonacci(1) + Fibonacci(2) = Fibonacci(1) + Fibonacci(0) + Fibonacci(1) = 1+1+1 = 3
'''
def misterio (n) :
    if (n ==1) :
        i=int( input ("Introduce un numero : ") )
        print (i)
    else :
        i=int( input ("Introduce un numero : ") )
        misterio (n -1)
        print (i)
    return
'''
'''
Si n es 1:
i = un núm (5)
printea el 6

Si n es mayor a 1:
Si n es 3
i = un num (2)
misterio(2)
print(2)

Si n es 2
i = un num (4)
misterio(1)
print(4)

si n es 1:
i = un num( 10)
printea el 10

Cómo va al revés, primero printea el 10, luego el 4 y luego el 2
print(misterio(3))
'''

'''
Suma del contenido de una lista
Quiero que empiece por la pos0

if pos ini < posfinal:
0 < 4
resultado = 1 + suma_lista(lista, 1, 4)
1 < 4
resultado = 2 + suma_lista(lista, 2, 4)
2 < 4
resultado = 3 + suma_lista(lista, 3, 4)
3 < 4
resultado = 4 + suma_lista(lista, 4, 4) = 4 + 5

resultado = 4 + 5 + 3 + 2 + 1 = 15 

'''

lista = [1,2,3,4,5]
def suma_lista(lista,posini,posfinal):
    if len(lista) == 0:
        resultado = 0
    if len(lista) == 1:
        resultado = lista[0]
    if posini == posfinal:
        resultado = lista[posini]
    else:
        resultado = lista[posini] + suma_lista(lista, posini+1, posfinal)
    return resultado

print(suma_lista(lista, 0, len(lista)-1))


