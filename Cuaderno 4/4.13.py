'''
Realizar un programa que lea palabras hasta que se introduzca “fin”, mostrando 
un recuento de las longitudes de las palabras, es decir, el número total de 
palabras de longitud 1 que se hayan introducido, el total de longitud 2, etc. La 
máxima longitud de las palabras deberá ser de 15 caracteres. Una posible salida 
de este programa sería: 
Palabras longitud 1: ninguna 
Palabras longitud 2: 10 
… 
Palabras longitud 15: 1
'''
lista_cuenta = [0]*15
texto = input("Introduce una palabra")

while texto != "fin":
    for i in range(1,16):
        if i == len(texto):
            lista_cuenta[i-1] += 1    
    texto = input("Introduce otra palabra")

for k in range (1, 16):
        print(f"Palabras de longitud {k} = {lista_cuenta[k-1]}")