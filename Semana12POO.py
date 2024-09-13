class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    # devolver un libro
    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                break

    # mostrar la información del usuario
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

# Clase Biblioteca que gestiona libros y usuarios
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    # agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    # registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # prestar un libro a un usuario
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros.pop(isbn)
            self.usuarios[id_usuario].prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {self.usuarios[id_usuario].nombre}.")
        else:
            print("No se pudo prestar el libro. Verifique el ID del usuario y el ISBN.")

    # devolver un libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.devolver_libro(isbn)
            print(f"El usuario '{usuario.nombre}' ha devuelto el libro con ISBN {isbn}.")
        else:
            print(f"No se encontró al usuario con ID {id_usuario}.")

    # buscar un libro por título
    def buscar_libro(self, titulo):
        for libro in self.libros.values():
            if libro.titulo.lower() == titulo.lower():
                print(f"Libro encontrado: {libro}")
                return
        print(f"No se encontró el libro con título '{titulo}'.")

    # mostrar los libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"No se encontró al usuario con ID {id_usuario}.")

# Código de prueba para usar la biblioteca
if __name__ == "__main__":
    biblioteca = Biblioteca()

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234567890")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "9876543210")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    usuario1 = Usuario("Elena Sanchez", 1)
    biblioteca.registrar_usuario(usuario1)

    biblioteca.prestar_libro(1, "1234567890")

    biblioteca.listar_libros_prestados(1)

    biblioteca.buscar_libro("Don Quijote de la Mancha")

    biblioteca.devolver_libro(1, "1234567890")

    biblioteca.listar_libros_prestados(1)