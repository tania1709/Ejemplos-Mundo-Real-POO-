class GestorDeMemoria:
    # Constructor (__init__)
    def __init__(self, tamaño):
        """
        Inicializa el objeto GestorDeMemoria con el tamaño de la memoria.
        """
        self.tamaño = tamaño
        self.memoria = [None] * tamaño
        self.asignaciones = {}
        print(f"Constructor: Se ha creado un objeto GestorDeMemoria con tamaño {tamaño}")

    # Destructor (__del__)
    def __del__(self):
        """
        Destructor: Se llama cuando el objeto es eliminado. Libera la memoria asignada.
        """
        print(f"Destructor: Se ha liberado la memoria asignada")
        del self.memoria
        del self.asignaciones

    # Método  para asignar memoria
    def asignar_memoria(self, nombre, tamaño):
        """
        Asigna memoria para el objeto con el nombre y tamaño especificados.
        """
        if tamaño <= self.tamaño:
            for i in range(self.tamaño):
                if self.memoria[i] is None:
                    self.memoria[i] = nombre
                    self.asignaciones[nombre] = i
                    print(f"Se ha asignado memoria para {nombre} en la posición {i}")
                    return
            print(f"Error: No hay suficiente memoria disponible")
        else:
            print(f"Error: El tamaño de la memoria es demasiado grande")

    #Método para liberar memoria
    def liberar_memoria(self, nombre):
        """
        Libera la memoria asignada para el objeto con el nombre especificado.
        """
        if nombre in self.asignaciones:
            posición = self.asignaciones[nombre]
            self.memoria[posición] = None
            del self.asignaciones[nombre]
            print(f"Se ha liberado la memoria para {nombre} en la posición {posición}")
        else:
            print(f"Error: No se ha asignado memoria para {nombre}")

    #Método para mostrar la memoria asignada
    def mostrar_memoria(self):
        """
        Muestra la memoria asignada para cada objeto.
        """
        print("Memoria asignada:")
        for nombre, posición in self.asignaciones.items():
            print(f"{nombre}: posición {posición}")

# Crear un objeto GestorDeMemoria
gestor = GestorDeMemoria(10)

# Asignar memoria para objetos
gestor.asignar_memoria("obj1", 2)
gestor.asignar_memoria("obj2", 3)
gestor.asignar_memoria("obj3", 1)

# Mostrar la memoria asignada
gestor.mostrar_memoria()

# Liberar memoria para un objeto
gestor.liberar_memoria("obj2")

# Mostrar la memoria asignada
gestor.mostrar_memoria()

# Eliminar el objeto (llamar al destructor)
del gestor
