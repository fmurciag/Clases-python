from ..separacion import Membranas


class Nano(Membranas):
    def __init__(self, eficiencia, area, presion_operacion, tamanio_poros):
        super().__init__(eficiencia, area, presion_operacion)
        self.tamanio_poros = tamanio_poros
