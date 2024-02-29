h = int(input ("¿Qué hora es en España?\n"))
m = int(input ("¿Y los minutos?\n"))


def hora_americana (h,m):
    '''
    '''
    hora_americana = h-12
    if 12 <= h <= 24:
        print (f"En formato 12 horas serían las {hora_americana}:{m}")
    elif 0 <= h < 12:
        print (f"Son las {h}:{m}")
    else:
        print("Ingresa una hora válida payaso")
        
print(hora_americana(h,m))