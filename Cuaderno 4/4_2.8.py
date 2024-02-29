'''
Realiza una aplicación que permita sumar dos matrices de tamaño 3x4. Las matrices 
contienen datos sobre Puntos2D. Debe hacer las siguientes tareas:
a. Solicitar datos para la matriz A.
b. Solicitar datos para la matriz B.
c. Presentar el resultado de matriz A + matriz B

Matriz = [][][][]
         [][][][]
         [][][][]

Matriz = (([][][][]), ([][][][]), ([][][][]))

'''
MatrizA = []
MatrizB = []
Suma_matrices = []

P1_A = 1, 2
P2_A = 3, 5
P3_A = 2,9
P4_A = 0, 3
P5_A = 6, 9
P6_A = 0, -2

MatrizA.append((P1_A, P2_A, P3_A, P4_A, P5_A, P6_A))

P1_B = 2, 8
P2_B= 2, -5
P3_B = 6,5
P4_B = 7, 0
P5_B = 6, -4
P6_B = 9, -2
MatrizB.append((P1_B, P2_B, P3_B, P4_B, P5_B, P6_B))


for i in range (6):
    for j in range(2):
        Suma_matrices.append(MatrizA[0][i][j] + MatrizB[0][i][j])

print(MatrizA)
print(MatrizB)
print(Suma_matrices)

print(MatrizA[0])