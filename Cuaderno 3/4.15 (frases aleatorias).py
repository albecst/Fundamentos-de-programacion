'''
Escriba un programa modularizado en Python que genere 5 frases a partir de 
palabras en la siguiente lista: 
['perro','niño','nube','padre','es','esta','come','mira','ama','el','la','al','en']
Las frases, que deben tener entre 3 y 10 palabras, deben generarse eligiendo un 
número aleatorio de palabras cada vez, de modo que la primera frase puede tener 
3 palabras, mientras que la segunda podría tener 6 palabras. Una vez generada 
una frase, el programa la mostrará por pantalla. Y así hasta 5 frases en total.
'''
import random
lista = ['perro ','niño ','nube ','padre ','es ','esta ','come ','mira ','ama ','el ','la ','al ','en ']
palabras = random.randint(0,12)
npalabras = random.randint(3,11)
frase = ""
cuenta = 0
while cuenta < 5:
    npalabras = random.randint(3,11)
    for i in range (1,npalabras+1):
        palabra = random.randint(0,12)
        frase = lista[palabra] + frase
    cuenta = cuenta + 1
    print(frase.capitalize())
    frase = ""

