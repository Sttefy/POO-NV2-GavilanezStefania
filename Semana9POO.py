class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def mostrar_informacion(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                self.productos.remove(producto)
                return True
        return False

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if nombre:
                    producto.set_nombre(nombre)
                if cantidad:
                    producto.set_cantidad(cantidad)
                if precio:
                    producto.set_precio(precio)
                return True
        return False

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos(self):
        for producto in self.productos:
            print(producto.mostrar_informacion())


# Ejemplo de uso:
inventario = Inventario()

# Añadir productos al inventario
productos = [
    Producto(2, "Arroz", 50, 0.65),
    Producto(3, "Azúcar", 30, 1.50),
    Producto(4, "Sal", 35, 0.85),
    Producto(5, "Aceite", 43, 1.85),
    Producto(6, "Yogurth", 32, 0.90),
    Producto(7, "Cereales", 20, 1.00),
    Producto(8, "Galletas", 57, 0.50),
    Producto(9, "Gomitas", 80, 0.25),
    Producto(10, "Huevos", 100, 0.15),
    Producto(11, "Avena", 50, 0.60),
    Producto(12, "Harina", 50, 0.50),
    Producto(13, "Gaseosas", 37, 1.25),
    Producto(14, "Detergente", 24, 1.00),
    Producto(15, "Cloro", 24, 1.25),
    Producto(16, "Jabón", 24, 0.80),
    Producto(17, "Fundas de basura", 36, 1.80),
    Producto(18, "Tragos", 24, 5.80)
]

# Agregar los productos al inventario
for producto in productos:
    inventario.agregar_producto(producto)

# Mostrar todos los productos en el inventario
inventario.mostrar_todos()

# Actualizar un producto
inventario.actualizar_producto(10, nombre="Huevos Grandes", cantidad=95, precio=0.20)

# Mostrar todos los productos nuevamente después de la actualización
print("\nDespués de la actualización:")
inventario.mostrar_todos()

# Buscar productos por nombre
print("\nBuscando productos que contienen 'arro':")
resultados = inventario.buscar_producto_por_nombre("arro")
for producto in resultados:
    print(producto.mostrar_informacion())
