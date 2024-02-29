def volumen (n,presion, temperatura):
    '''
    float, float, float --> float
    OBJ: calcular el volumen de una gas ideal en base a su presión y a su temperatura
    PRE: P > 0, T > 0
    '''
    R = 0.082 #atmósferas
    return n*R*temperatura/presion

print(f"{volumen(1,2,180)} L")