def fuerza (masa, aceleración):
    '''
    float, float ----> float
    OBJ: calcular la fuerza en base a la masa y a la aceleración
    PRE: masa > 0
    '''
    return(masa * aceleración)

masa = 60 #kg
aceleración = 9.8 #m/s**2

print(f"{fuerza(masa, aceleración)} N")

print((fuerza(masa,aceleración)), "N")