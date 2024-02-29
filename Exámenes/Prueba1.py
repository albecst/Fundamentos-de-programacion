#Ejercicio 1
opcion = input("\nIntroduce un número del 0 al 3. \nSi presiona 1, podrá verificar si un número es par y/o si tiene 4 cifras. \nSi presiona 2, podrá comprobar si un número es par y de cuatro cifras. Además, ese número se elevará al cuadrado y sacará las centena, unidades de mil, decenas de mil y centenas de mil. \nSi presiona 3, calculará el factorial de un número. \nPor último, si presiona el 0 saldrá del programa. \nIntroduce el número: ")

if opcion == "1":
    n = int(input("Introduce un número entero: "))
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
    if 1000 <= n <= 9999:
        print("Tiene 4 cifras")
    else:
        print("No tiene 4 cifras")
    
if opcion == "2":
    m = int(input("Introduce un número entero par que tenga 4 cifras: "))
    if m % 2 == 0 and 1000 <= m <= 9999:
        print("Es par y tiene 4 cifras")
    else:
        print("Este número no es correcto")
    
    m2 = m**2
    print(f"Este número al cuadrado es igual a {m2}")
    m2_str = str(m2)
    print(f" Centenas: {m2_str[5]}")
    print(f" Unidades_de_mil: {m2_str[4]}")
    print(f" Decenas de mil: {m2_str[3]}")
    print(f" Centenas de mil: {m2_str[2]}")    
    
    
    
if opcion == "3":
    factorial = 1
    ñ = int(input("Introduce un número entero por pantalla: "))
    for i in range (1, ñ+1):
        factorial = factorial * i
    print(factorial)
        
if opcion == "0":
    print("Ha salido del programa. Vuelva a ejecutarlo si quiere realizar alguna operación")

if opcion != "1" and opcion != "2" and opcion != "3":
    print("GILIPOLLAS DEL 0 al 3")