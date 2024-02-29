'''
Escriba un programa que “codifique” una frase modificando todas las vocales 
según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el símbolo #. 
Por ejemplo, la frase: “Un perro del hortelano”, deberá devolverse: “#n p3rr0 d3l 
h0rt3l4n0”
'''

frase = "un perro del hortelano"
frase = list(frase)
print(frase)

for i in range(len(frase)):
    if frase[i] == "a":
        frase[i] = "4"
    if frase[i] == "e":
        frase[i] = "3"
    if frase[i] == "i":
        frase[i] = "1"
    if frase [i] == "o":
        frase [i] = "0"
    if frase [i] == "u":
        frase [i] = "#"

frase = "".join(frase)   
print(frase)
