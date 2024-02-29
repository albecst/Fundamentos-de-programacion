'''
Calcular la suma de los números pares entre 0 y n de manera recursiva. 

#Si n = 6
resultado = 6 + 4 + 2 + 0
#Si n = 10
resultado = 10 + 8 + 6 + 4 + 2 + 0
'''

def suma_pares(n):
    '''
    '''
    if n // 2 == 0:
        resultado = 0
    else:
        resultado = n + suma_pares(n-2)
    return resultado
print(suma_pares(10))

'''
4 // 2 = 2
resultado = 4 + suma_pares(2)
2 // 2 = 1
resultado = 2 + suma_pares(0)
0 // 2 == 0
resultado = 0

resultado = 4 + 2 + 0
'''