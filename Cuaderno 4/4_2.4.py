'''
Implementa una estructura que de soporte a los puntos en 2D, es decir, con dos 
coordenadas x e y. Programa después funciones para su suma y resta.
'''
coordenadas = []
x = 2, 3, 5, 8, 1, 3, 0
y = 2, 4, 9, 1, 4, 8, 3
coordenadas.append((x, y))
print(coordenadas)

def suma_de_coordenadas(coordenadas):
    '''
    lista -> int
    OBJ:
    '''
    suma = 0
    for i in range(len(x)):
        suma = x[i] + y[i]
        print(suma, end = " / ")
    return "= SUMAS"

def resta_de_coordenadas(coordenadas):
    '''
    lista -> int
    OBJ:
    '''
    resta = 0
    for i in range(len(x)):
        resta = x[i] - y[i]
        print(resta, end = " / ")
    return "= RESTAS"

print(suma_de_coordenadas(coordenadas))
print(resta_de_coordenadas(coordenadas))