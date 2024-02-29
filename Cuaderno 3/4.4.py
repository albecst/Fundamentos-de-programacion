'''
Escribe un programa que lea una serie de números enteros hasta que se 
introduzca el número -9999, y cuente el total de números introducidos, el total de 
valores positivos y el total de valores negativos (no consideres el cero ni positivo ni 
negativo). Reutiliza la función que hayas diseñado en el Ejercicio 1 para validar tus 
entradas.
'''

n = int(input("Introduce un número entero.\n"))

def lector_de_numeros(n):
 """ None --> int
 OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo
 cuando se ha asegurado de que es realmente un entero
 """
 positivos = 1
 negativos = -1
 numeros = 0
 
 while n != -9999:
     numeros = numeros + 1
     n = int(input("Introduce un número entero"))
     if n < 0:
         negativos = negativos + 1
     if n > 0:
         positivos = positivos + 1
         
 print(f"Hay {positivos} números positivos")
 print(f"Hay {negativos} números negativos")
 print(f"Hay {numeros} numeros")
 
print(lector_de_numeros(n))