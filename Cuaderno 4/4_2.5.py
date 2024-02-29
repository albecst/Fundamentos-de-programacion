'''
Programa una función distancia_2D que calcule la distancia entre dos puntos. La función 
retornará un número real según la siguiente fórmula:
raíz((x2-x1)^2 + (y2-y1)^2)
'''

puntos = {"p1":(2, 3), "p2":(1, 4)}

def distancia_2D(puntos):
    '''
    '''
    distancia = ((puntos["p2"][0] - puntos["p1"][0])**2 + (puntos["p2"][1] - puntos["p1"][1])**2)**0.5
    return distancia

print(distancia_2D(puntos))


