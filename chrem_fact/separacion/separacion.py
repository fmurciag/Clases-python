class Separacion:
    def __init__(self, eficiencia):
        self.eficiencia = eficiencia

    def determinar_pureza(self):
        print("Determinando pureza del proceso de separación")

    def simular(self):
        print(f"Simulando proceso de separación con eficiencia del {self.eficiencia}%")

    def calcular_coste_operativo(self, energia_consumida, costo_energia):
        return energia_consumida * costo_energia


class Membranas(Separacion):
    def __init__(self, eficiencia, area, presion_operacion):
        super().__init__(eficiencia)
        self.area = area
        self.presion_operacion = presion_operacion

    def calcular_flujo_transmembrana(self):
        print("Calculando flujo a través de la membrana")


class Columnas(Separacion):
    def __init__(self, eficiencia, numero_platos, altura):
        super().__init__(eficiencia)
        self.numero_platos = numero_platos
        self.altura = altura

    def calcular_reflujo(self):
        print("Calculando relación de reflujo en la columna")

    def estimar_capacidad_produccion(self, flujo_alimentacion, eficiencia_separacion):
        return flujo_alimentacion * eficiencia_separacion
