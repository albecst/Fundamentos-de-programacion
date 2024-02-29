'''
2. La varianza poblacional de una población p, que dispone de n elementos se define 
como: 
∑
(𝒑𝒊 − 𝒑𝒎𝒆𝒅𝒊𝒂)
𝟐
𝒏 − 𝟏
𝒏
𝒊=𝟎
Construye un subprograma que devuelva la varianza de una población que recibe 
como parámetro. 
'''

poblaciones = [3, 6, 12, 18]
n = 4-1 #Porque empieza en el 0

def pmedia(pmedia0,n):
    pmedia0 = 0
    for j in range (0,n+1):
        pmedia0 = poblaciones[j] + pmedia0
    pmedia = (pmedia0)/(n+1)
    return pmedia
print(pmedia(0,3))
pmedia = pmedia(0,n)

def varianza_poblacion(pmedia, n):
    varianza0 = 0
    for i in range (0,n+1):
        varianza0 = varianza0 + ((poblaciones[i] - pmedia)**2)
    varianza = varianza0/(n)
    return varianza
print(varianza_poblacion(pmedia, 3))

