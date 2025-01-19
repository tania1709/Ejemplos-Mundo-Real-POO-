# Clase base: Ave
class Ave:
    def __init__(self, nombre, edad, plumas):
        self.__nombre = nombre
        self.__edad = edad
        self.__plumas = plumas

    # Método para obtener el nombre de la ave
    def get_nombre(self):
        return self.__nombre

    # Método para obtener la edad de la ave
    def get_edad(self):
        return self.__edad

    # Método para obtener el número de plumas de la ave
    def get_plumas(self):
        return self.__plumas

    # Método para volar
    def volar(self):
        print(f"{self.__nombre} está volando")

# Clase derivada: Pájaro
class Pajaro(Ave):
    def __init__(self, nombre, edad, plumas, canto):
        super().__init__(nombre, edad, plumas)
        self.__canto = canto

    # Método para obtener el canto del pájaro
    def get_canto(self):
        return self.__canto

    # Método para cantar
    def cantar(self):
        print(f"{self.get_nombre()} está cantando: {self.__canto}")

# Crear instancias de las clases
pajaro1 = Pajaro("Tweety", 1, 100, "Pío pío")
pajaro2 = Pajaro("Sylvester", 2, 50, "Grito grito")

# Utilizar métodos de las clases
pajaro1.volar()
pajaro1.cantar()
print(f"Nombre: {pajaro1.get_nombre()}, Edad: {pajaro1.get_edad()}, Plumas: {pajaro1.get_plumas()}, Canto: {pajaro1.get_canto()}")

pajaro2.volar()
pajaro2.cantar()
print(f"Nombre: {pajaro2.get_nombre()}, Edad: {pajaro2.get_edad()}, Plumas: {pajaro2.get_plumas()}, Canto: {pajaro2.get_canto()}")
