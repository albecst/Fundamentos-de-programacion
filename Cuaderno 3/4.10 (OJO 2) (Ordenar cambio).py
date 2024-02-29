'''
.Cada país acuña billetes y monedas de unos determinados valores. Por ejemplo, en 
los países de la Unión Europea los valores son: 500.0, 200.0, 100.0, 50.0, 20.0, 
10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 euros. Diseña un subprograma 
para una caja de un supermercado, el cual reciba un importe en euros y la 
cantidad pagada por el cliente en una compra y muestre al cajero cuántas piezas 
(billetes y monedas) y de qué tipo debe dar como cambio. Dicha salida no deberá 
en ningún caso especificar piezas para las que haya que dar cero unidades.
'''

#Por ej, si son 120 euros de cambio me tiene que dar 1 de 100, 1 de 20.
#Cambio = dinero_total - gasto

tipos = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

cambio = 10214

for x in range(0, len(tipos)):
    cantidad = 0
    while cambio >= tipos[x]:
        cambio = (cambio - tipos[x])
        cantidad += 1
    if cantidad > 0:
        print(f"{cantidad} billetes/monedas de {tipos[x]} euros")
