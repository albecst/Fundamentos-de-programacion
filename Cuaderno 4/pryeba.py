def frecuencias_palabras():
    # Define un diccionario vacío para almacenar las frecuencias de las longitudes de las palabras
    frecuencias = {}

    # Utiliza un bucle while para leer palabras de la entrada estándar hasta que se introduzca "fin"
    while True:
        palabra = input("Introduce una palabra (o 'fin' para terminar): ")
        if palabra == "fin":
            break

        # Obtiene la longitud de la palabra
        longitud = len(palabra)

        # Si la longitud de la palabra ya está en el diccionario, incrementa su frecuencia en 1
        if longitud in frecuencias:
            frecuencias[longitud] += 1
        # De lo contrario, agrega una nueva entrada al diccionario con la longitud de la palabra como clave y una frecuencia de 1 como valor
        else:
            frecuencias[longitud] = 1

    # Devuelve el diccionario de frecuencias de las longitudes de las palabras
    return frecuencias

print(frecuencias_palabras())