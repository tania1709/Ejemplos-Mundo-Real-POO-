
# Clase Producto

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


# Clase Inventario

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if self.buscar_producto_id(producto.get_id()) is None:
            self.productos.append(producto)
            print(f"Producto {producto.get_nombre()} agregado con éxito.")
        else:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")

    def eliminar_producto(self, id):
        producto = self.buscar_producto_id(id)
        if producto is not None:
            self.productos.remove(producto)
            print(f"Producto con ID {id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró un producto con el ID {id}.")

    def actualizar_cantidad(self, id, cantidad):
        producto = self.buscar_producto_id(id)
        if producto is not None:
            producto.set_cantidad(cantidad)
            print(f"Cantidad del producto con ID {id} actualizada con éxito.")
        else:
            print(f"Error: No se encontró un producto con el ID {id}.")

    def actualizar_precio(self, id, precio):
        producto = self.buscar_producto_id(id)
        if producto is not None:
            producto.set_precio(precio)
            print(f"Precio del producto con ID {id} actualizado con éxito.")
        else:
            print(f"Error: No se encontró un producto con el ID {id}.")

    def buscar_producto_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_producto_nombre(self, nombre):
        productos_encontrados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                productos_encontrados.append(producto)
        return productos_encontrados

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

# Interfaz de Usuario

def menu_principal():
    inventario = Inventario()
    while True:
        print("\nMenú Principal:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto por ID")
        print("6. Buscar producto por nombre")
        print("7. Mostrar todos los productos")
        print("8. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)
        elif opcion == "4":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar_precio(id, precio)
        elif opcion == "5":
            id = int(input("Ingrese el ID del producto a buscar: "))
            producto = inventario.buscar_producto_id(id)
            if producto is not None:
                print(producto)
            else:
                print("No se encontró el producto.")
        elif opcion == "6":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto_nombre(nombre)
            if productos_encontrados:
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "7":
            inventario.mostrar_productos()
        elif opcion == "8":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()