'''
RECURSIVIDAD
Definir un objeto o proceso en funcion de si mismo.
Es util para resolver problemas por descomposicion en subproblemas.
Los subproblemas tienen identica estructura al problema original, pero
el caso que resuelven esta reducido o es mas pequeño.

Básicamente, el programa se llama a sí mismo.
'''
def factorial(n):
    '''
    '''
    if n == 0:
        resultado = 1
    else:
        resultado = n*factorial(n-1)
    return resultado

print(factorial(3))


#Multiplicar dos números por sumas sucesivas
#1º Cualquier número multiplicado por 1 es ese numero (4*1 = 4)
#Ej. para multiplicar 3*6, podemos hacer 2*6+6, 1*6+6+6
def sumas_sucesivas(n,m):
    if n == 1:
        resultado = m
    else:
        resultado = m + sumas_sucesivas(n-1, m)
    return resultado

print(sumas_sucesivas(4, 6))

#Fibonacci
#1, 1+1, 1+2, 2+3, 3+5...

def fibonacci(n):
    '''
    '''
    if n == 0 or n == 1:
        resultado = 1
    else:
        resultado = fibonacci(n-2) + fibonacci(n-1)
    return resultado

print(fibonacci(6))


#Imprime al revés, porque la llamada recursiva se hace de final hacia principio
def misterio(n) :
    if (n ==1) :
        i=int( input ("Introduce un numero : ") )
        print (i)
    else :
        i=int( input ("Introduce un numero : ") )
        misterio (n -1)
        print (i)
    return

print(misterio(3))

#Palíndromos
def es_palíndromo(pal, posini, posfin):
    if posini >= posfin:
        resultado = True
    else:
        if pal[posini] != pal[posfin]:
            resultado = False
        else:
            resultado = es_palíndromo(pal, posini+1, posfin-1)
    return resultado    

print(es_palíndromo("rallar", 0, 5))

#Suma del contenido de una lista

def suma_lista(lista, inicio, final):
    '''
    '''
    if len(lista) == 0:
        resultado = 0
    elif inicio == final:
        resultado = lista[inicio]
    else:
        resultado = lista[inicio] + suma_lista(lista, inicio+1, final)
    return resultado

print(suma_lista([1,2,3,4], 0, 3))

#Mostrar elementos

def mostrar_elementos(lista, inicio, final):
    if len(lista) == 0:
        print(lista)
    elif inicio == final:
        print(lista[final])
    else:
        print(lista[inicio]) 
        mostrar_elementos(lista, inicio+1, final)
    return

print(mostrar_elementos([1,2,3,4,5], 0, 4))

#EJERCICIOS PROPUESTOS

'''
1. Codificar un modulo recursivo que calcule la division entera entre dos
numeros A y B sin utilizar multiplicaciones ni divisiones
'''
#Ej 6/3 es lo mismo que restar 2 veces 3 a 6 (3-3=0)
#a = 6
#b = 3
#6/3 = 2

def division_entera(a, b):
    if a == b:
        resultado = 1
    if a < b:
        resultado = 0
    else:
        resultado = division_entera(a-b, b) + 1
    return resultado
print(division_entera(10, 6))    
    
'''
2.Codificar un modulo recursivo que calcule x^n con x real y n entero.
'''
#2^3 es lo mismo que multiplicar 2*2*2

def x_elevado_n (x, n):
    '''
    '''
    if n == 1:
        resultado = x
    elif n == 0:
        resultado = 1
    else:
        resultado = x * x_elevado_n(x, n-1)
    return resultado

print(x_elevado_n(2,4))

'''
3. Codificar un programa recursivo que toma una cadena como
parametro y devuelve otra cadena que es la original pero con sus
caracteres invertidos.
'''
#buenas uenas enas nas as s

def cadena_inversa(texto, pinicial, pfinal):
    '''
    '''
    if len(texto) <= 1:
        texto = texto[pinicial]
    elif pinicial == pfinal:
        print(texto[pfinal])
    else:
        texto = texto[pfinal] + cadena_inversa(texto, pinicial+1, pfinal)
    return texto

print(cadena_inversa("buenas", 0, len("buenas")))

'''
4. Los detectives de una agencia se envían todos los mensajes cifrados
por motivos de seguridad. El algoritmo que están utilizando en la
actualidad consiste en intercambiar cada vocal por la letra que la
precede (si existe). Por ejemplo: El resultado de codificar el mensaje:
esta en Leon
esate n eoLn
'''
