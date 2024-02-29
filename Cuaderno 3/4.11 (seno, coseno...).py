'''
Escribe un programa, ahora con estructuras repetitivas, que muestre un menú en 
pantalla que permita calcular el seno, coseno, tangente, cotangente, secante y 
cosecante de un ángulo. El menú se mostrará hasta que el usuario decida salir, y 
mientras permitirá hacer todas las operaciones que desee el usuario. El menú 
quedará así: 
1. Seno
2. Coseno
...
0. Salir
Elija una opción:
Sugerencia: El menú podría estar centrado, utiliza las bibliotecas ya realizadas.
'''

import math

ángulo = int(input("Introduce el ángulo: \n"))
función = input("¿Qué quieres calcular?:\n1. Seno \n2. Coseno \n3. Tangente \n4. Cotangente \n5. Secante \n6. Cosecante \n0. Salir \nIntroduzca el número correspondiente a cada operación: ")

while función != "0":
    if función == "1":
        print(math.sin(math.radians(ángulo)))
    elif función == "2":
        print(math.cos(math.radians(ángulo)))
    elif función == "3":
        print(math.tan(math.radians(ángulo)))
    elif función == "4":
        math.cotan = math.tan(math.radians(ángulo))**-1
        print(math.cotan)
    elif función == "5":
        math.sec = math.cos(math.radians(ángulo))**-1
        print(math.sec)
    elif función == "6":
        math.cosec = math.sin(math.radians(ángulo))**-1 
        print(math.cosec)
    función = input("\n¿Qué quieres calcular ahora?:\n1. Seno \n2. Coseno \n3. Tangente \n4. Cotangente \n5. Secante \n6. Cosecante \n0. Salir \nIntroduzca el número correspondiente a cada operación: ")

    