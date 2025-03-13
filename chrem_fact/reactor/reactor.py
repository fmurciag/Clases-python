from result import Result


class Reactor:
    def __init__(self, volumen, temperatura, presion):
        self.volumen = volumen
        self.temperatura = temperatura
        self.presion = presion

    def simular(self):
        print(
            f"Simulando reactor con volumen {self.volumen} m3, temperatura {self.temperatura}°C y presión {self.presion} atm"
        )

        return Result()

    def calcular_conversion(self, reaccion):
        print(f"Calculando conversión para la reacción {reaccion}")

    def calcular_energia_reaccion(self, entalpia_reaccion, cantidad_reactivo):
        return entalpia_reaccion * cantidad_reactivo


class Descontinuo(Reactor):
    def __init__(self, volumen, temperatura, presion, tiempo_reaccion):
        super().__init__(volumen, temperatura, presion)
        self.tiempo_reaccion = tiempo_reaccion

    def determinar_fin_reaccion(self):
        print("Evaluando si la reacción ha finalizado")


class Continuo(Reactor):
    def __init__(self, volumen, temperatura, presion, caudal_entrada, caudal_salida):
        super().__init__(volumen, temperatura, presion)
        self.caudal_entrada = caudal_entrada
        self.caudal_salida = caudal_salida

    def calcular_tiempo_residencia(self):
        return self.volumen / self.caudal_entrada
