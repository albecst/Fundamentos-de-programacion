import math

def raíz_cuadrada(a,b,c):
    '''
    '''
    return (b**2-4*a*c)**1/2

def ecuación_segundo_grado(a,b,c):
    '''
    '''
    return((-b+math.sqrt(b**2-4*a*c))/2*a,(-b-math.sqrt(b**2-4*a*c))/2*a )

print(ecuación_segundo_grado(1,2,-3))

