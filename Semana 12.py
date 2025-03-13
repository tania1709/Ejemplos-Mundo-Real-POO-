# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} de {self.autor}, categoría {self.categoria}, ISBN {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID {self.id_usuario})"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()
        self.usuarios_registrados = {}

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios.add(usuario.id_usuario)
        self.usuarios_registrados[usuario.id_usuario] = usuario

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_registrados[id_usuario]

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_registrados[id_usuario]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"El libro {libro.titulo} ha sido prestado a {usuario.nombre}")
            else:
                print(f"El libro {libro.titulo} ya ha sido prestado a {usuario.nombre}")

    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_registrados[id_usuario]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"El libro {libro.titulo} ha sido devuelto")
            else:
                print(f"El libro {libro.titulo} no ha sido prestado a {usuario.nombre}")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo is None or libro.titulo == titulo) and \
               (autor is None or libro.autor == autor) and \
               (categoria is None or libro.categoria == categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            return usuario.libros_prestados
        return []

# Prueba del sistema
biblioteca = Biblioteca()

libro1 = Libro("La Sombra del Viento", "Carlos Ruiz. Zafón", "Ficción", "978-84-01-01343-9")
libro2 = Libro("El Poder del Ahora", "Eckhart Tolle", "Espiritualidad", "978-84-01-01344-6")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("Sofía Lema", 1)
usuario2 = Usuario("Gabriela Fernandez", 2)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro(libro1.isbn, usuario1.id_usuario)
biblioteca.prestar_libro(libro2.isbn, usuario2.id_usuario)

print("Libros prestados a Sofía Lema:")
for libro in biblioteca.listar_libros_prestados(usuario1.id_usuario):
    print(libro)

print("Libros prestados a Gabriela Fernandez:")
for libro in biblioteca.listar_libros_prestados(usuario2.id_usuario):
    print(libro)

biblioteca.devolver_libro(libro1.isbn, usuario1.id_usuario)

print("Libros prestados a Sofía Lema después de devolver un libro:")
for libro in biblioteca.listar_libros_prestados(usuario1.id_usuario):
    print(libro)
