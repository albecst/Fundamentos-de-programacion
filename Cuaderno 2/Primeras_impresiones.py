def discriminante(a, b, c):
    '''
    float,float,float --> float
    OBJ: calcula el discriminante de la ecuación de segundo grado 
    '''
    return pow(b**2-4*a*c,0.5)
 
#Probador 4,5,1
print(discriminante(4,5,1))


#Ver si un nº es par o impar
def par_impar(a):
    '''
    x
    '''
    if a % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
        
a = int(input("Escribe un nº y te diré si es par o impar\n"))
print(par_impar(a))