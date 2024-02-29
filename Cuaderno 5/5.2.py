'''
Implementar un programa que dados dos números, calcule el producto de 
forma recursiva. Los números a multiplicar deben ser leídos por teclado. 
NOTA: no puede utilizar el operador de multiplicación así que utilice sumas.

3*3 = 3 + 3*2 = 3 + 3 + 3*1
3*1 = 3
3*0 = 0
'''

def suma_recursiva(m, n):
    if n == 1:
        resultado = m
    elif n == 0:
        resultado = 0
    elif n > 1:
        resultado = m + suma_recursiva(m, n-1)
    return resultado

print(suma_recursiva(3,5))


