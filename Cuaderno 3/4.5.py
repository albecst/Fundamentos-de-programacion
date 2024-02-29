'''
Implementa una variante del Ejercicio Resuelto 3 que dibuje en pantalla un 
rectángulo de dimensiones dadas pero con dos símbolos, las filas pares con ‘@’ y 
las impares con ‘#’. Esta será la versión “3a”. Después de hacerlo, crea una 
segunda versión “3b” para que esta vez los símbolos se alternen en las columnas, 
es decir, las columnas pares se dibujarán con ‘@’ y las impares con ‘#’.
'''

def rectángulo3a (n,m): #n filas m columnas
    for i in range (1, n+1): #Si n = 3, que lo haga en la fila 1, 3, 5
        if i % 2 != 0:
            print("#"*m)
        if i % 2 == 0:
            print("@"*m)

def rectángulo3b (n,m):
    for j in range (1, m+1):
        if j % 2 != 0:
            print("#"*n,"\n")
        if j % 2 == 0:
            print("@"*n)
print(rectángulo3b(4,4))