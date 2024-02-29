texto_numerico = "45" #Hemos elegido el carácter 45 (como string), en vez del número 45 como int

int (texto_numerico) #Convertimos el 45 (que antes era string) a int

int ("Hola") #Aquí encontramos un error, ya que hemos pasado el "Hola" como texto a un número entero, algo que no tiene mucho sentido

int (3.99999) #Se olvida de todos los decimales y se centra en el número sin decimal, en este caso el 3

int(-3.99999) #Idem

float (34) #Básicamente, pasamos el 34 como int al 34 como float (es decir, al 34.0)

int("diez") #Encontramos el mismo error que con el "Hola"