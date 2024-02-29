'''
Escribe un programa que, después de preguntar ¿Cuántos números se van a 
introducir?, pida esos números (enteros o reales) y devuelva su media aritmética, 
el mayor y el menor. El programa debe controlar que la cantidad de números es 
mayor de 2 y en caso contrario ha de mostrar un mensaje de error. Como siempre, 
valida las entradas.
'''

N = int(input("¿Cuántos números se van a introducir?\n"))
contador = 0
n = 0
mayor = 0
menor = 10**100

if N >= 2:
    while contador < N:
        contador = contador + 1
        a = int(input("Introduce el número: "))
        n = n + a
        if a > mayor:
            mayor = a
        if a < menor:
            menor = a
            
    media = n/N
    print(media)
else:
    print("Debes introducir más números para hacer su media.")
    
print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")

