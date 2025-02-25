from .bomba import Bomba


class Centrifuga(Bomba):
    def __init__(self, potencia, eficiencia, velocidad_rotacion):
        super().__init__(potencia, eficiencia)
        self.velocidad_rotacion = velocidad_rotacion

    def calcular_presion_salida(self):
        print("Calculando presión de salida de la bomba centrífuga")

    def calcular_potencia_requerida(self, caudal, altura):
        return (caudal * altura * self.velocidad_rotacion) / 102
