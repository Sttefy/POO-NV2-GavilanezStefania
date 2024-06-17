# Ejemplo mundo real

class Usuario:
    def __init__(self, nombre, apellido, edad, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cargo = cargo

    def __str__(self):
        return f'Usuario {self.nombre}, con apellido {self.apellido}, tiene {self.edad} años, con un cargo de {self.cargo}'

class Computadora:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.usuario = None

    def asignar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            self.usuario = usuario

    def __str__(self):
        return f'Computadora {self.marca} de modelo {self.modelo}, tiene un sistema operativo {self.sistema_operativo}, operado por {self.usuario}'

# Crear instancias de Usuario y Computadora
mi_usuario = Usuario('Fernando', 'Cabrera', 23, 'Gerente')
mi_computadora = Computadora('HP', 'Envy', 'Windows 10')

# Asignar el usuario a la computadora
mi_computadora.asignar_usuario(mi_usuario)

# Imprimir información de la computadora y del usuario
print(mi_computadora)
print(mi_usuario)