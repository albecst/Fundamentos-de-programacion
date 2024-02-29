

def segundos(h,m,s):
    '''
    int, int, int --> int
    OBJ: calcular los segundos que han pasado desde las 00:00
    PRE: 0 < h < 24, 0 < m or s < 60
    '''
    s = h*3600+m*60+s
    return s

h = int(input("Introduce la hora: \n"))
m = int(input("Introduce los minutos:  \n"))
s = int(input("Introduce los segundos:  \n"))

print(segundos (h,m,s))

    

