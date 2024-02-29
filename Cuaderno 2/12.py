def redondeo (nota):
    '''
    '''
    if int(nota) < nota <= int(nota) + 0.24:
        print(int((nota)))
    if int(nota) + 0.24 < nota <= int(nota) + 0.5:
        print(int((nota)) + 0.5)
    if int(nota) + 0.5 < nota <= int(nota) + 0.75:
        print(int(nota) + 0.5)
    if int(nota) + 0.75 <= nota <= int(nota) + 1:
        print(int(nota) + 1)

print(redondeo(7.35))

