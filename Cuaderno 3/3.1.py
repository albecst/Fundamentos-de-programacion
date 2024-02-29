precio_compra = 102 #€


try:
    precio_compra = float(precio_compra) 

except:
    print("MÉTETE EL TEXTO POR EL CULO")

else:
        
    if precio_compra > 100:
        tarjeta = input("¿Vas a pagar con tarjeta o efectivo? \n")    
        if (tarjeta == "Tarjeta"):
            precio_final_tarjeta = precio_compra*98/100
            print("Tendrás un 2 por ciento de descuento, el precio final es",precio_final_tarjeta, "€")
        elif (tarjeta == "Efectivo"):
            precio_final_efectivo = precio_compra*95/100
            print("Tendrás un 5 por ciento de descuento, el precio final es",precio_final_efectivo, "€")
        else:
            print("\nNo te he entendido, ¿te has equivocado escribiendo? \nPrueba con una mayúscula al principio de la palabra. \n")
    else:
        precio_final_efectivo = precio_compra
        print(precio_final_efectivo)
        precio_final_tarjeta = precio_compra
        print(precio_final_efectivo)
        
        