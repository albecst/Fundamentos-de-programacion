'''
Escribir una función que permita mostrar los caracteres de una cadena del final 
al principio, pero nunca mostrando la letra “a”. Ejemplo: si la entrada es “barco 
amarillo”, la función devolverá: “ollirm ocrb”.
'''

texto = "barco amarillo"
posini = 0
posfin = len(texto) - 1

while posini <= posfin:
    if texto[posfin] != "a":
        print(texto[posfin], end = "")
    posfin -= 1
    