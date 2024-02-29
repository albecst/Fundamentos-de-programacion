def tabla_de_multiplicar(n):
    '''
    int --> int
    OBJ:
    PRE: n>0
    ''' 
    print(f"                    Tabla de multiplicar del 1 al {n}: ")
    print(f"                    ---------------------------------- ")

    
    for i in range (1, n+1):
        for j in range (1, n+1):
            numero = i*j
            print(f"{numero}", end = "\t")
        print()
        
print(tabla_de_multiplicar(10))
                    
