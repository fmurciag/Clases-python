from ..reactor import Continuo


class PFR(Continuo):
    def __init__(self, volumen, temperatura, presion, caudal_entrada, caudal_salida, longitud, diametro):
        super().__init__(volumen, temperatura, presion, caudal_entrada, caudal_salida)
        self.longitud = longitud
        self.diametro = diametro

    def calcular_perdida_carga(self):
        print("Calculando pérdida de carga en el reactor PFR")

    def determinar_rendimiento_reactor(self, conversion, selectividad):
        return conversion * selectividad
