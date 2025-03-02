#Clase Producto

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


#Clase Inventario

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado")

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].cantidad = cantidad
        else:
            print("Producto no encontrado")

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].precio = precio
        else:
            print("Producto no encontrado")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)


#Almacenamiento en Archivos

import json

def guardar_inventario(inventario, archivo):
    datos = []
    for producto in inventario.productos.values():
        datos.append({
            "id": producto.id,
            "nombre": producto.nombre,
            "cantidad": producto.cantidad,
            "precio": producto.precio
        })
    with open(archivo, "w") as f:
        json.dump(datos, f)

def cargar_inventario(archivo):
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
        inventario = Inventario()
        for dato in datos:
            producto = Producto(dato["id"], dato["nombre"], dato["cantidad"], dato["precio"])
            inventario.agregar_producto(producto)
        return inventario
    except FileNotFoundError:
        return Inventario()


#Interfaz de Usuario

def menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Actualizar precio")
    print("5. Buscar producto")
    print("6. Mostrar productos")
    print("7. Guardar inventario")
    print("8. Cargar inventario")
    print("9. Salir")

def main():
    inventario = Inventario()
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            id = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = input("Ingrese ID: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese ID: ")
            cantidad = int(input("Ingrese cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)
        elif opcion == "4":
            id = input("Ingrese ID: ")
            precio = float(input("Ingrese precio: "))
            inventario.actualizar_precio(id, precio)
        elif opcion == "5":
            nombre = input("Ingrese nombre: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado")
        elif opcion == "6":
            inventario.mostrar_productos()
        elif opcion == "7":
            archivo = input("Ingrese nombre de archivo: ")
            guardar_inventario(inventario, archivo)
        elif opcion == "8":
            archivo = input("Ingrese nombre de archivo: ")
            inventario = cargar_inventario(archivo)
        elif opcion == "9":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()