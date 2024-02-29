'''
Escribe un programa que lea dos caracteres y averigüe si se introdujeron en el 
orden de su código ASCII o no. Se deberá además comprobar si el primero de ellos 
es una cifra, y en caso afirmativo indicar si es impar y si es o no primo. Modulariza
la solución. En tu código no deben aparecer los valores de la tabla ASCII, porque 
produciría un código muy difícil de mantener, puedes usar ord() y chr() o 
simplemente saber que en la tabla ASCII todos los dígitos son consecutivos).
'''

def comprobar(a,b):
    '''
    '''
    return chr(a) + 1 == chr(b)

print(comprobar(2, 3))