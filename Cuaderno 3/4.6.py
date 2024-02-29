'''
Escribe un programa que pida un número límite y calcule cuántos términos de la 
serie armónica son necesarios para que su suma supere dicho límite. Es decir, 
dado un límite se trata de determinar el menor número n tal que:
1 + 1/2 + 1/3 + ... 1/n > limite

Prueba tu código, y ten en cuenta que para valores altos del límite el tiempo de 
cálculo se dispara. Así, para un límite = 5, n sería 83; para 10 ya asciende a 
12.367 y para 15, ¡¡el número de términos es 1.835.421!! El programa ha de ser 
robusto y controlar que el número introducido es un entero positivo.
'''
'''
def numero_de_terminos(n):
    ''
    ''
    termino = 1
    suma = 1
    for i in range (2, n+1):
        suma = suma + 1/i
        termino = termino + 1
    print(1/suma)
    print(termino)
    
print(numero_de_terminos(83))

'''        
def numero_limite_real(limite):
    '''
    '''
    termino = 1
    suma = 1
    n = 1
    while suma < limite:
        n = n+1
        suma = suma + 1/n
        termino = termino + 1
    print(termino)
    print(suma)

print(numero_limite_real(15))
