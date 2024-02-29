'''
Implementa una aplicación que solicite 10 valores y los almacene en un contenedor. A 
continuación, tu aplicación recorrerá el contenedor restándole a cada valor el valor que  
se encuentre en la siguiente posición (ej.: [1, 3, 5], resultado [(1-3), (3-5), (5-1)] = -2, -2,
4). Modulariza tu solución
'''

valores = []
resultados = []
n = 10
for i in range(n):
    valor = int(input("Introduce un valor"))
    valores.append(valor)
    
for j in range(n-1):
    resultado = valores[j] - valores[j+1]
    resultados.append(resultado)

print(valores)
print(resultados)