class Implementos:
    def __init__(self, maquinas, telas, cortadora, tijeras, tizas):
        self.maquinas = maquinas
        self.telas = telas
        self.cortadora = cortadora
        self.tijeras = tijeras
        self.tizas = tizas

    def mostrar(self):
        return f'Implementos: {self.maquinas}, {self.telas}, {self.cortadora}, {self.tijeras} y {self.tizas}'

class Maquinas:
    def __init__(self, recta, overlok, recubridora, enlasticadora):
        self.recta = recta
        self.overlok = overlok
        self.recubridora = recubridora
        self.enlasticadora = enlasticadora

    def mostrar_informacion(self):
        return f'Máquinas: {self.recta}, {self.overlok}, {self.recubridora} y {self.enlasticadora}'

mi_taller_tiene_las_siguientes_maquinas = Maquinas("recta", "overlok", "recubridora", "enlasticadora")
print(mi_taller_tiene_las_siguientes_maquinas.mostrar_informacion())

class Pagos:
    def __init__(self, pago_operarios, pago_proveedores):
        self.__pago_operarios = pago_operarios
        self.__pago_proveedores = pago_proveedores

    def pagar_operarios(self, sueldo):
        if sueldo > 0:
            self.__pago_operarios -= sueldo

    def pagar_proveedores(self, pago):
        if pago > 0:
            self.__pago_proveedores -= pago

    def obtener_saldos(self):
        return f'Saldo operarios: {self.__pago_operarios}, Saldo proveedores: {self.__pago_proveedores}'

class EquiposElectronicos:
    def encender(self):
        return "Equipos electrónicos encendiéndose"

class Computadora(EquiposElectronicos):
    def encender(self):
        return "Computadora encendida y arrancando"

class Camara(EquiposElectronicos):
    def encender(self):
        return "Cámara encendida y grabando"

# Instancias y uso de clases
mi_computadora = Computadora()
mi_camara = Camara()

print(mi_computadora.encender())
print(mi_camara.encender())

# Ejemplo de uso de la clase Pagos para mostrar encapsulamiento
pagos = Pagos(5000, 3000)
print(pagos.obtener_saldos())

# Realizando pagos
pagos.pagar_operarios(500)
pagos.pagar_proveedores(1000)
print(pagos.obtener_saldos())
