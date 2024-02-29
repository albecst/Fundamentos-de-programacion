'''
1. Ya vimos que la validación de entradas es algo tan presente que no podemos 
escapar de ello, así que si te parece vamos a escribir una función que solicite al 
usuario introducir un entero y que no pare de pedírselo hasta que la información 
introducida sea válida. 
La idea es usar la construcción while combinada con la función de validación 
programada en cuadernos anteriores, consiguiendo una función cuya cabecera 
sería la siguiente:
'''            

n = float(input("Introduce un número entero.\n"))

def leer_entero_validado(n):
 """ None --> int
 OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo
 cuando se ha asegurado de que es realmente un entero
 """

 while n != int(n):
    n = float(input("Eso no es un número entero, intentalo de nuevo. \n"))
 n = int(n)
 print(f"Es correcto, {n} es un número entero.")
 return

print(leer_entero_validado(n))