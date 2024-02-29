'''
Escribe una función y su probador para calcular el factorial de un número validado 
en el rango de 0 a 30.
'''

def factorial(n):
    '''
    int --> int
    OBJ: calcular factorial
    PRE: 0 <= n <= 30
    '''
    acumulacion = 1
    for i in range (1, n+1):
        acumulacion = acumulacion * i
    return acumulacion

print(factorial(4))
print(factorial(27))
print(factorial(10))

'''
Programa un subprograma que utilizando bucles for anidados muestre por 
pantalla la siguiente salida:
1 - 0 1 - 1 1 - 2 1 - 3
2 - 0 2 - 1 2 - 2 2 - 3
3 - 0 3 - 1 3 - 2 3 - 3
'''

for i in range (1, 4):
    for j in range (0, 4):
        print(f"{i} - {j}", end = '\t')
    print(end = "\n")
    
'''
Programa un procedimiento que dibuje en pantalla un rectángulo de dimensiones 
dadas con un símbolo que se le especifica. 
Por ejemplo, la llamada al  procedimiento dibujar_rectangulo(3,5,"#") produciría la siguiente salida:
#####
#####
#####
'''

def rectángulo(n, m, simbolo):
    '''
    int, int, str --> none
    OBJ: dibujar un rectángulo nxm lleno del símbolo
    '''
    for i in range (n):
        print(simbolo*m)
                
print(rectángulo(3,2, "|"))

'''
4. Implemente un sencillo juego que haga al usuario adivinar un carácter oculto. 
'''

intento = 1
print("Intente adivinar el símbolo oculto")
simbolo = input("Cuál crees que es \n")
while simbolo != "#":
    intento = intento + 1
    simbolo = input(f"Es incorrecto, prueba de nuevo. Va usted por el intento número {intento} \n")
print(f"Bien hecho, lo ha conseguido en el intento {intento}")
 