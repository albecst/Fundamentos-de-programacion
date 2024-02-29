def gas_ideal(presion,temperatura):
    '''
    float, float --> string
    OBJ: comprobar si un gas es un gas ideal
    PRE: presion, temperatura > 0
    '''
    if (temperatura == 273.15 and presion == 1):
        print("Nos encontramos ante un gas ideal")
    else:
        print("No es un gas ideal")


print(gas_ideal(1, 273.15))