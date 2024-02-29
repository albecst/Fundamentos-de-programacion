'''
Un texto contiene comandos en forma de frases separadas por puntos. En cada 
frase, la primera palabra contiene el código de la operación y la última el 
resultado. Ejemplo: 
SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. Etc. 
Cree una lista de parejas [código-resultado] utilizando como entrada un texto 
con el formato indicado.
'''

texto = "SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. Etc."
lista_parejas = []
lista_parejas2 = []
lista_parejas3 = []
div = texto.split(".")
print(div[0], "\n", div[1], "\n", div[2], "\n")
lista_parejas.append(div[0][0:5])
lista_parejas.append(div[0][12:14])

lista_parejas2.append(div[1][1:4])

print(lista_parejas)
print(lista_parejas2)
