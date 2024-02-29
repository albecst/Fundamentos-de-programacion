'''
Una compañía de alquiler de automóviles desea adquirir un programa para emitir 
sus facturas, con las siguientes consideraciones:
a. Se factura una cantidad fija de 100EUR si no se rebasan los 300 Km.
b. Si la distancia recorrida es mayor que 300 Km, entonces:
i. Si la distancia es menor o igual que 1.000 Km, se cobrarán 100EUR
más el kilometraje que exceda de 300 Km, a razón de 30 
céntimos/Km.
ii. Si la distancia es mayor que 1.000 Km, se cobrarán los 100EUR más 
el kilometraje a razón de 30 céntimos/Km para los kilómetros entre 
el 300 y el 1.000 y 20 céntimos/Km para el resto.
'''

#100 euros si x < 300
#Si 300 < x < 1000, 100 euros más los kilometros a 0.3 euros por kilometro.
#Si x > 1000, 100 + 0.3 euros por km hasta los 1000, 0.2 euros por km para más de 1000

km = float(input("¿Cuántos km has hecho? \n"))

def pago(km):
    '''
    float, float --> float
    OBJ: calcular el dinero que hay que pagar a una compañía de automoviles dependiendo de cuántos km hagas
    PRE: d > 0
    '''
    precio = 100 #€
    precio21 = precio + 0.3*(km-300)
    precio22 = precio + 700*0.3
    precio3 = precio22 + 0.2*(km-1000)
    
    if km < 300:
        print(f"{precio} euros")
    elif 300 <= km <= 1000:
        if km < 1000:
            print(f"{precio21} euros")
        elif km >= 1000:
            print(f"{precio22} euros")
    if km > 1000:
        print(f"{precio3} euros")

print(pago(km))