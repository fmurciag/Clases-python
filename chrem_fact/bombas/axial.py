from bomba import Bomba


class Axial(Bomba):
    def __init__(self, potencia, eficiencia, angulo_aspas):
        super().__init__(potencia, eficiencia)
        self.angulo_aspas = angulo_aspas

    def calcular_direccion_flujo(self):
        print("Calculando dirección del flujo en la bomba axial")
