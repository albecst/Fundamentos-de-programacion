def centrarRotulo (rotulo):
 """string--> None
 OBJ: centra rótulo, subrayado con signos =, +línea encima y debajo
 """
 tam=len(rotulo)
 lado=((72-tam)//2)-1 # 72 columnas suele ser ancho de la pantalla
 print()
 print(' '*lado,rotulo)
 print(' '*lado , '='*tam , end='\n')

#Probador
frase = 'Don Quijote de la Mancha' 
centrarRotulo(frase) # distinto nombre
centrarRotulo('Cervantes') # constante
rotulo = 'El famoso hidalgo don Quijote de la Mancha' # mismo nombre
centrarRotulo(rotulo)