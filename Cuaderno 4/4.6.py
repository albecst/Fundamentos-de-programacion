'''
Implementar una función que compruebe si una palabra es un palíndromo. 
Atención, no hagas más trabajo del necesario.
'''

palabra = "ananana"
ult = len(palabra)-1
pos = 0
rango = int(len(palabra)/2) 

while palabra[pos] == palabra[ult]:
    ult = ult - 1
    pos = pos + 1
    print(ult, pos)
    print(palabra[ult], palabra[pos])

if palabra[pos] == palabra[ult]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")