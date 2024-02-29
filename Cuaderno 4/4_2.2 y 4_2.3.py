'''
Programa un software que utilice lo programado en el ejercicio 1 para leer los datos de 
10 personas y calcule la media de edad general, la media por sexo, la cantidad de 
mujeres que tienen entre 13 y 16 años y el número de hombres menores de 20 años.
1. Leer los datos de 10 personas
2. Media de edad
3. Media por sexo
4. Mujeres entre 13 y 16
5. Hombres menores de 20
6. Amplía el ejercicio anterior mostrando al final del proceso los datos completos de la mujer y el hombre más jóvenes de todos los introducidos.
'''

# Definir una lista vacía para almacenar los datos de las personas
personas = []

# Leer los datos de las 10 personas
nombre = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"
edad = 1, 2, 3, 4, 5, 6, 7, 8, 2, 14
sexo = "M", "M", "H", "M", "H", "H", "H", "M", "H", "M" 
personas.append((nombre, edad, sexo))

# Calcular la media de edad general
suma = 0
cuenta = 0
for i in range(len(edad)):
    suma += edad[i]
    cuenta += 1
media = suma/cuenta
print(media)

# Calcular la media de edad por sexo
edad_mujeres = 0
edad_hombres = 0
cuenta_mujeres = 1
cuenta_hombres = 1

for i in range(len(edad)):
    if sexo[i] == "H":
        edad_hombres += edad[i]
        cuenta_hombres += 1        
    elif sexo[i] == "M":
        edad_mujeres += edad[i]
        cuenta_mujeres += 1
media_edad_hombres = edad_hombres/cuenta_hombres
media_edad_mujeres = edad_mujeres/cuenta_mujeres
print(media_edad_hombres)
print(media_edad_mujeres)
  

# Calcular la cantidad de mujeres que tienen entre 13 y 16 años
cantidad_mujeres_entre_13_16 = 0
for i in range(len(sexo)):
    if sexo[i] == "M":
        if 13 < edad[i] < 16:
            cantidad_mujeres_entre_13_16 += 1 
print(cantidad_mujeres_entre_13_16)

# Calcular el número de hombres menores de 20 años
cantidad_hombres_menores_20 = 0
for persona in personas:
    if persona[2] == "M" and persona[1] < 20:
        cantidad_hombres_menores_20 += 1
        
# 6)
edad_min_hombre = 1000
edad_min_mujer = 1000
x = 0
y = 0
for i in range(len(sexo)):
    if sexo[i] == "H":
        if edad[i] < edad_min_hombre:
            edad_min_hombre = edad[i]
            x = i
    if sexo[i] == "M":
        if edad[i] < edad_min_mujer:
            edad_min_mujer = edad[i]
            y = i
print(f"Edad del hombre más joven: {edad[x]} años, Nombre: {nombre[x]}")
print(f"Edad de la mujer más joven: {edad[y]} años, Nombre: {nombre[y]}")