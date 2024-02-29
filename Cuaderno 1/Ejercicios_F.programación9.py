'''      
#9
b = 3.16
c = 4.879
x = 6.666
'''

a = 3/2
b= 3.0/2
c = 3 // 2


print(type(a))
print(type(b))
print(type(c))
print(a, b, c)

fruta = "ciruela"
tipo = "claudia"
print(fruta + tipo)
print(fruta * 3)

#Elif es poner elif varias veces if
a = int(input("Introduce un número cualquiera\n"))
if a < 0:
    print("Es un número menor que 0")
elif 0 <= a <= 5:
    print("Ese número está entre el 0 y el 5")
elif a > 5:
    print ("Ese número es mayor que 5")
    
#Si a = True, da False.
#Si a = False, da True.
a = a == False

print(1 and not 2 or 3)

