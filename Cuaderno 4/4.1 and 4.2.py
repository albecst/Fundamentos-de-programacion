'''
1.Escribir una función que sume dos listas de enteros de igual longitud y retorne 
otra lista que contenga la suma de las originales elemento a elemento. 

2. Modifica la función anterior permitiendo que las listas sean desiguales. Los 
elementos sobrantes de la lista más larga se añadirán al final de la lista 
resultante. 
'''
#1
suma = [0]*4
lista1 = [1,2,3,4]
lista2 = [4,3,2,1]

for i in range(len(lista1)):
    suma[i] = lista1[i] + lista2[i]
print(suma)

#2
lista3 = [1,2,3,4,5,6,7]
lista4 = [6,9,14]
suma = [0]*len(lista4)

pos = 0
while pos < len(lista4):
    suma[pos] = lista3[pos] + lista4[pos]
    pos += 1

suma = suma + lista3[pos:]

print(suma)