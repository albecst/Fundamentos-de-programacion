#A notas >= 8.5
#B 6.5 >= notas > 8.5
#C 5 >= notas > 6.5
#D 3.5 >= notas > 5
#F 0 >= notas > 3.5

notas = input("Qué nota has sacado\n")

try:
    notas = float(notas)
except:
    print("Estás metiendo texto")

else:
    if 8.5 <= notas < 10:
        print("Has sacado un A")
    elif 6.5 <= notas < 8.5:
        print("Has sacado un B")
    elif 5 <= notas < 6.5:
        print("Has sacado un C")
    elif 3.5 <= notas < 5:
        print("Has sacado un D")
    elif 0 <= notas < 3.5:
        print("Has sacado un F")
    else:
        print("Eres un payaso, mete una nota válida anda")