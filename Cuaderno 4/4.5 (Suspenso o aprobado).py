'''
Modificar una lista de números reales que representan las calificaciones de los 
alumnos de una clase, para sustituir los valores numéricos por sus calificaciones 
alfanuméricas (Suspenso, Aprobado, etc.) 
'''

notas = [1, 3, 6, 4, 9, 2, 5, 4, 7, 2, 4, 8, 3, 7, 9, 3]

for i in range(len(notas)):
    if 0 < notas[i] < 5:
        notas[i] = "Suspenso"
    else:
        notas[i] = "Aprobado"
print(notas)
