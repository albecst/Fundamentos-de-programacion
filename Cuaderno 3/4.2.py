'''
Una mejora útil, al anterior ejercicio, es programar una función entero_pedido 
(min, max, msj) que pedirá un entero pero limitará su rango, es decir, el entero 
deberá estar comprendido entre un máximo y un mínimo. Además, la función 
recibirá un mensaje que será el que empleará para interactuar con el usuario.
Como ayuda, te ponemos aquí cómo sería el probador:
'''

n = float(input("Introduce un número entero.\n"))

def entero_pedido(min, max, n):
    '''
    '''
    if min <= n <= max:
        while n != int(n):
            n = float(input("Eso no es un número entero, intentalo de nuevo. \n"))
        print(f"Es correcto, {int(n)} es un número entero que está entre {min} y {max}.")
    else:
        while n > max or n < min: 
            n = int(input(f"Introduce un número entero válido que esté entre {min} y {max}. \n"))
        print(f"Es correcto, {int(n)} es un número entero que está entre {min} y {max}.")
        
#Probador
min = 1
max = 12
n = int(n)
print(entero_pedido(min, max, n))