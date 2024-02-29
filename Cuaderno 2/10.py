def año_bisiesto(año):
    '''
    '''
    
    if((año % 400 == 0) and (año % 100 == 0)):
        print("Es un año bisiesto")
    elif (año % 100 == 0):
        print("No es un año bisiesto")
    elif (año % 4 == 0):
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")    

print(año_bisiesto(500))