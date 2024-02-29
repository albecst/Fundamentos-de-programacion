'''
Realiza un programa para gestionar los datos de stock de una tienda de 
comestibles. La información a recoger será: nombre de producto, precio y
cantidad de stock. La tienda dispone de 10 productos distintos. El programa 
debe ser capaz de:
a. Dar de alta un producto nuevo
b. Buscar un producto por su nombre, empleando búsqueda secuencial.
c. Ordenar los productos por el método de la burbuja según su precio.
'''
Productos = []

Producto1 = {"Nombre": "B", "Precio": 30, "Cantidad de stock": 100}
Producto2 = {"Nombre": "A", "Precio": 40, "Cantidad de stock": 200}
Producto3 = {"Nombre": "C", "Precio": 129, "Cantidad de stock": 6450}
Producto4 = {"Nombre": "E", "Precio": 208, "Cantidad de stock": 320}
Producto5 = {"Nombre": "D", "Precio": 200, "Cantidad de stock": 6350}
Producto6 = {"Nombre": "I", "Precio": 543, "Cantidad de stock": 3340}
Producto7 = {"Nombre": "G", "Precio": 442, "Cantidad de stock": 220}
Producto8 = {"Nombre": "F", "Precio": 2000, "Cantidad de stock": 100}
Producto9 = {"Nombre": "H", "Precio": 602, "Cantidad de stock": 10}
Producto10 = {"Nombre": "J", "Precio": 2240, "Cantidad de stock": 1110}


Productos = [Producto1, Producto2, Producto3, Producto4, Producto5, Producto6, Producto7, Producto8, Producto9, Producto10]
Existe = None

# a)
a = input("Introduce el nombre del nuevo producto: ")
b = int(input("Introduce su precio: "))
c = int(input("Introduce su cantidad de stock: "))
Producto4 = {"Nombre": a, "Precio":b, "Cantidad de stock":c}
Productos.append(Producto4)

# b)
new_nombre = input("Introduce el producto que quieres buscar: ")
for i in range(len(Productos)):
    if Productos[i]["Nombre"] == new_nombre:
        print(f"El producto está en la posición {Productos.index(Productos[i])}")
        Existe = True

if Existe == None:
    print("Ese producto no existe en nuestra despensa.")    
  
# c)
def burbuja(Productos):
    '''
    list --> None
    OBJ: ordenar los productos mediante el método de la burbuja dependiendo de su precio
    '''
    for i in range(len(Productos)):
        for j in range(len(Productos)-1, 0, -1):
            if Productos[j-1]["Precio"] < Productos[j]["Precio"]:
                Productos[j-1], Productos[j] = Productos[j], Productos[j-1]
    return Productos

print(burbuja(Productos))
