#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2],
         'UWU131HD': [349990,1], 
         'FS1230HD': [249990,0],
}


def stock_marca(marca):
    cant=0
    for modelo,dato in productos.items():
        if marca==dato[0]:
            # print(marca)
            #     # print (modelo)
            for cod, detalle in stock.items():
                if modelo==cod:
                    # print(detalle)
                    cant+=detalle[1]
    print(f"El stock es: ",cant)


def busqueda_precio(p_min, p_max):
    lista=[]
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if cantidad>0 and (p_min<=precio<=p_max):
            for model, info in productos.items():
                if model==modelo:
                    lista=[modelo, info[0]]
                    lista.sort()
            print(f"Modelo: ",lista[0],  "--- Marca: ", lista[1])
      
                
def eliminar_producto(modelo):
    if modelo in productos: 
       productos.pop(modelo)
       if modelo in stock:
           stock.pop(modelo)
           return True
    return False
    


# Menu Principal ----------------------------------

opcion=1
while opcion!=4:
    
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca")
    print("2. Búsqueda por precio.")
    print("3. Eliminar producto.")
    print("4. Salir.")

    try:
        opcion= int(input("Ingrese una opción: "))
    except ValueError:
        print("Debe ingresar un numero entero")
        continue

    match opcion:
        case 1: 
            marca=input("Ingrese marca a consultar: ")
            stock_marca(marca)
        case 2:
            while True:
                try:
                    p_min= int(input("Ingrese precio mínimo: "))
                    p_max= int(input("ingrese el precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!!")         
            busqueda_precio(p_min, p_max)
        case 3:
            while True:
                modelo= input("Ingrese modelo a eliminar: ")
                if modelo==True:
                    eliminar_producto(modelo)
                    print("Producto Eliminado!")
                    # print(productos)
                    # print(stock)
                else:
                    print("El modelo no existe!")
            

                otro= input("Desea eliminar otro producto? (si/no): ").lower()
                            
                if otro!="si":
                    print("Volviendo al Menu")
                    break
            
        case 4:
            print("Programa Finalizado.")
        case _:
            print("Debe seleccionar una opción válida!!!")
