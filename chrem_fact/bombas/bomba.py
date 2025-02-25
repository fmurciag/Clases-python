class Bomba:
    def __init__(self, potencia, eficiencia):
        self.potencia = potencia
        self.eficiencia = eficiencia

    def calcular_flujo(self):
        print("Calculando flujo de la bomba")

    def simular(self):
        print(f"Simulando bomba con potencia {self.potencia} kW y eficiencia {self.eficiencia}%")
