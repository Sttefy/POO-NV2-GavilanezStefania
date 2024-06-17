#Programacion_orientada_a_objetos_POO
class Temperatura:
    def __init__(self, fecha, valor):
        self.fecha = fecha
        self.valor = valor

    def promedio_diario(self, temperaturas):
        total = 0
        for temperatura in temperaturas:
            total += temperatura

        promedio = total / len(temperaturas)
        return promedio

temperaturas_diarias = [22.5, 24.2, 21.8, 25.7]

temperatura_promedio_diaria = Temperatura(None, None).promedio_diario(temperaturas_diarias)
print(f"Temperatura promedio diaria: {temperatura_promedio_diaria:.2f}°C")