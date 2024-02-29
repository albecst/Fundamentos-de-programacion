'''
En el baremo para la adjudicación de plazas en las Escuelas Infantiles Públicas se 
otorgan puntos en función de los ingresos de la unidad familiar, según se recoge 
en la siguiente tabla:
Puntos                  Ingresos/mes €      Hasta € (excluido)
                        Desde (incluido)    
1                       5000                ---
2                       3500                5000
3                       1800                3500
4                       0                   1800
Construye un subprograma que devuelva los puntos de un niño según los ingresos 
de su unidad familiar.
'''

dinero = float(input("¿Cuánto cobras? \n"))

def puntos (dinero):
    '''
    '''
    if 0 <= dinero < 1800:
        puntos = 4
        print(puntos)
    elif 1800 <= dinero < 3500:
        puntos = 3
        print(puntos)
    elif 3500 <= dinero < 5000:
        puntos = 2
        print(puntos)
    elif dinero >= 5000:
        puntos = 1
        print(puntos)

print(puntos(dinero))
    
