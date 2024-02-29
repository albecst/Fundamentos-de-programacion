'''
Haz un programa que pida al usuario un año, si lo introducido por el usuario es 
posterior a 1.582 imprimirá si es bisiesto, y si no, explicará el motivo. Recuerda 
reutilizar tu función es_bisiesto de cuadernos anteriores ¿Cuántas veces debes 
probar este ejercicio? 
'''

año = int(input("Introduce un año posterior a 1582 y te diré si es bisiesto o no"))

def año_bisiesto(año):
    '''
    '''
    if año < 1582:
        print("No rula, cambio de calendario hermano")
    if año >= 1582:
        if((año % 400 == 0) and (año % 100 == 0)):
            print("Es un año bisiesto")
        elif (año % 100 == 0):
            print("No es un año bisiesto")
        elif (año % 4 == 0):
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")    

print(año_bisiesto(año))