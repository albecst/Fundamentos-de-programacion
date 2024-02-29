#Variables: 
#Distancia recorrida (km)
#Litros gasoil utilizados
#Coste litros gasoil 
#Demás costes camión

#Necesito calcular:
#Km recorridos / litro
#Coste total viaje
#Coste total / km

#Datos
Distancia_recorrida = 1000 #km
Litros_gasoil_utilizados = 90 #L
Coste_LG = 1.80 * Litros_gasoil_utilizados #€
Demás_costes = 140 #€

#Ejecución
#Km/L
Distancia_recorrida_por_litros = Distancia_recorrida/Litros_gasoil_utilizados
print(Distancia_recorrida_por_litros, "Km/L")

#Coste total viaje
Coste_Total = Coste_LG + Demás_costes
print(Coste_Total)

#Coste total por km
Coste_Total_Km = Coste_Total/Distancia_recorrida
print(Coste_Total_Km, "€/km")