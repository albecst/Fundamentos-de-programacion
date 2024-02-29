


intento = 5
intentohaciadelante = 1
print("Intente adivinar el símbolo oculto")
simbolo = input("Cuál crees que es \n")
while simbolo != "#" and intento > 1:
        intentohaciadelante = intentohaciadelante + 1
        intento = intento - 1
        simbolo = input(f"Es incorrecto, prueba de nuevo. {intento} intento/s restante/s \n")
if simbolo == "#":
    print(f"Bien hecho, lo ha conseguido en el intento {intentohaciadelante}")
else:
    print(f"Vaya, inténtelo de nuevo")