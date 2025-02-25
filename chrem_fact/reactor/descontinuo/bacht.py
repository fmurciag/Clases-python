from reactor import Descontinuo


class Batch(Descontinuo):
    def __init__(self, volumen, temperatura, presion, tiempo_reaccion, carga_inicial):
        super().__init__(volumen, temperatura, presion, tiempo_reaccion)
        self.carga_inicial = carga_inicial

    def controlar_temperatura(self):
        print("Controlando temperatura en el reactor batch")
