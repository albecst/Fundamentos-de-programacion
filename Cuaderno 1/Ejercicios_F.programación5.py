#Segundos que tiene un día
Día = 86400 #s

#La hora es las 19:30:01
Hora_elegida = 60*60*19.30+1

#Si la medianoche es a las 00:00, y de 00:00 (día 1) a 00:00 (día 2) am hay 86400 s...
Tiempo_restante = Día - Hora_elegida
print("Quedan", Tiempo_restante, "s para que llegue medianoche")

#Si la anterior medianoche fue a las 00:00, han pasado...
Tiempo_pasado = Hora_elegida
print("Han pasado", Tiempo_pasado, "s")

# Tiempo_pasado + Tiempo_restante tienen que dar 86400 s
Díaprueba = Tiempo_restante + Tiempo_pasado
print(Díaprueba, "(Lo tienes bien)")