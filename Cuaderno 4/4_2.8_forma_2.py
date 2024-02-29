MatrizA = []
MatrizB = []
suma = []

#Para pedir los datos, necesito 3 filas (i) y 4 columnas (j)

for i in range(3):
    fila = []
    for j in range(4):
        x = int(input("Introduce valor A: "))
        fila.append(x)
    MatrizA.append(fila)
    
for k in range(3):
    filaB = []
    for l in range(4):
        x = int(input("Ahora introduce valor B: "))
        filaB.append(x)
    MatrizB.append(filaB)

print(MatrizA)
print(MatrizB)


for m in range(3):
    filasuma = []
    for n in range(4):
        filasuma.append(MatrizA[m][n] + MatrizB[m][n])
    suma.append(filasuma)    
    
print(suma)