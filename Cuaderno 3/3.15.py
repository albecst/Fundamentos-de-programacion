'''
Un monomio está caracterizado por un coeficiente (real) y una x elevada a un 
exponente (entero y positivo), si bien puede no llevar x. Como es sabido, un 
polinomio es una suma de monomios (Ejemplo: +2x**3 + x + 4.0 )
Para escribir en pantalla un monomio, hay que tener en cuenta que:
a. Si el coeficiente (a) es 0 no deberá imprimirse el monomio. 
b. Si el coeficiente (a) es 1 no imprimiremos el coeficiente. 
c. Si el exponente (n) es 1 no escribiremos el exponente
d. Si el exponente (n) es 0 no escribiremos ni el polinomio ni la x. 
Haz un subprograma que imprima un monomio. Advierte que Python no escribe el 
“+” en los números positivos y ahora hará falta hacerlo expresamente.
'''
print("\n")
print("Antes de nada quiero que sepas que distinguimos entre números positivos y negativos. Si quieres poner un número negativo tendrás que escribir el -.\n")
a = int(input("Introduce el coeficiente \n"))
n = int(input("Introduce el exponente \n"))

def monomio(a,n):
    '''
    '''
    if a == 0 and n == 0 and n == 1 and n != 1:
        print("")
    elif a == 1 and n != 0 and n!= 1:
        print(f"x**{n}")
    elif a != 0 and a != 1:
        if n == 0:
            print(a)
        elif n == 1:
            print(f"{a}x")
        elif n != 0 and n != 1:
            print(f"{a}x**{n}")
    
    
print(monomio(a,n))