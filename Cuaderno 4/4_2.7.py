'''
Implementa una aplicación para ayudar en la gestión de cobros de una gasolinera. 
Mediante 3 listas deberá calcular el gasto de un total de 10 clientes. La primera lista será 
utilizada para almacenar el gasto de cada cliente en gasolina, la segunda para almacenar 
el gasto en productos de la tienda de la gasolinera, y la tercera lista almacenará la suma 
de las dos anteriores. La aplicación solicitará por teclado los gastos de gasolina y de la 
tienda para cada uno de los 10 clientes.
'''

gastos_gasolina = []
gastos_tienda = []
suma_gastos = []

for i in range(10):
    gasolina = int(input("Introduce tu gasto en gasolina: "))
    tienda = int(input("Introduce tu gasto en la tienda: "))
    gastos_gasolina.append(gasolina)
    gastos_tienda.append(tienda)
    suma_gastos.append(gastos_gasolina[i] + gastos_tienda[i])

print(gastos_gasolina)
print(gastos_tienda)
print(suma_gastos)
