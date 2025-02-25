from reactor import Continuo


class CSTR(Continuo):
    def __init__(self, volumen, temperatura, presion, caudal_entrada, caudal_salida, agitacion):
        super().__init__(volumen, temperatura, presion, caudal_entrada, caudal_salida)
        self.agitacion = agitacion

    def calcular_mezcla(self):
        print("Calculando nivel de mezcla en CSTR")
