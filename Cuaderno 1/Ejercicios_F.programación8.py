def área_rectángulo(altura, base):
    '''
    float, float --> float
    OBJ: Calcular el perímetro del rectángulo con la altura y la base
    PRE: altura > 0; base > 0
    '''
    return (base * altura)

def perímetro_rectángulo(altura, base):
    '''
    float, float --> float
    OBJ: Calcular el perímetro del rectángulo con la altura y la base
    PRE: altura > 0; base > 0
    '''
    return(2*altura + 2*base)


base = 6
altura = 8
print(área_rectángulo(altura,base))
print(f"El perímetro del rectángulo es {perímetro_rectángulo(altura, base)}")
