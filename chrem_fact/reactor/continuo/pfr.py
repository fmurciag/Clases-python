from ..reactor import Continuo
from result import Result


class PFR(Continuo):
    def __init__(
        self, volumen, temperatura, presion, caudal_entrada, caudal_salida, longitud, diametro, **composiciones
    ):
        super().__init__(volumen, temperatura, presion, caudal_entrada, caudal_salida)
        self.longitud = longitud
        self.diametro = diametro
        self.composiciones = composiciones

    def reacacionar(self):
        suma = 0
        for comp in self.composiciones:
            suma += self.composiciones[comp]
            print(f"Reaccionando {comp}, {self.composiciones[comp]}")
        return suma

    def calcular_perdida_carga(self):
        print("Calculando pérdida de carga en el reactor PFR")

    def determinar_rendimiento_reactor(self, conversion, selectividad):
        return conversion * selectividad

    def simular(self):
        return Result(prcentaje_reaccionado=self.reacacionar())
