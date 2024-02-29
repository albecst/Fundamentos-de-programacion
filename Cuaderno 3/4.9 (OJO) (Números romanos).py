def convertir_a_romano(num):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numero_romano = ''
    i = 0
    while num > 0:
        for _ in range(num // valores[i]):
            numero_romano += simbolos[i]
            num -= valores[i]
        i += 1
    return numero_romano

# Prueba el programa con un número
print(convertir_a_romano(1987)) # Debería imprimir MCMLXXXVII
