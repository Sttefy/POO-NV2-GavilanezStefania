class Router:
    def __init__(self, tamaño, color, marca, modelo):
        self.tamaño = tamaño
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'Router(tamaño={self.tamaño}, de color={self.color}, es de marca={self.marca}, tiene el modelo={self.modelo})'

    def __del__(self):
        print(f'El router {self.modelo} esta eliminado')


El_router = Router("Pequeño", "blanco", "Huawei", "EG8M8145V5G32")
print(El_router)

