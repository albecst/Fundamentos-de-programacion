'''
Mejore el programa anterior para que genere, no 5 frases, sino tantas como sea 
necesario hasta que alguna de ellas tenga sentido. Para ello, después de generar 
una frase e imprimirla por pantalla se preguntará al usuario si considera que la 
frase generada tiene sentido y, si su respuesta es afirmativa, mostrará un mensaje 
final indicando el número de frases generadas hasta que se obtuvo una con
sentido
'''

import random
lista = ['perro ','niño ','nube ','padre ','es ','esta ','come ','mira ','ama ','el ','la ','al ','en ']
palabras = random.randint(0,12)
npalabras = random.randint(3,11)
frase = ""
cuenta = 0
oraciones = 1

pregunta2 = input("¿Estás preparado para jugar?: ")

if pregunta2 == "Si":
    npalabras = random.randint(3,11)
    for i in range (1,npalabras+1):
        palabra = random.randint(0,12)
        frase = lista[palabra] + frase
    print(frase.capitalize())
    
    pregunta = input("¿Tiene sentido esta oración?: ")
    
    while pregunta != "Si" or pregunta == "No":
        npalabras = random.randint(3,11)
        for i in range (1,npalabras+1):
            palabra = random.randint(0,12)
            frase = lista[palabra] + frase
        print(frase.capitalize())
        frase = ""
        oraciones = oraciones + 1
        pregunta = input("¿Tiene sentido esta oración?: ")
    print(f"Se han generado {oraciones} oraciones")

else:
    print(f"Payaso")


