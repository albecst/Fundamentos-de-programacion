'''
Escribe un programa que lea un entero positivo n y genere una tabla con las n
primeras potencias de 2, 3 y 5. Así:
1 2 4 8 16 32 64 ...
1 3 9 27 81 243 729 ...
1 5 25 125 625 3125 15625 ...
'''
#Básicamente, que si pongo n = 5, que me ponga 5 primeras potencias de 2, 3 y 5 (Sería 1,2,4,8,16 ; 1,3,9,27,81; 1,5,25,125,625)

#Imaginamos que tomamos el 0 como primera potencia (2**0 = 1)
def primeras_potencias(n):
    '''
    float --> float
    OBJ:
    '''

    for i in range (0, n):
        resultado2 = 2**i
        print(f"{resultado2}", end = " ")
    print()
        
    for j in range (0, n):
        resultado3 = 3**j
        print(f"{resultado3}", end = " ")
    print()
    
    for k in range (0, n):
        resultado5 = 5**k
        print(f"{resultado5}", end = " ")
    print()

print(primeras_potencias(6))