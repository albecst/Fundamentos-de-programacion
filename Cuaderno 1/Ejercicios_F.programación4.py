#Variables
ingresos_totales = 1600 #€
n_hijos = 2 #Hijos
ingreso_imponible = ingresos_totales - 600 - 60*n_hijos 
impuesto = ingreso_imponible/3

#Programa
print(impuesto,"€")