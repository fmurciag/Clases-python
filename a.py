import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


class Vehiculo:
    def __init__(self, marca, modelo, ano, kilometraje, en_venta):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilometraje = kilometraje
        self.en_venta = en_venta

    # def poner_en_venta()
    def __str__(self):
        return f"{self.marca}, {self.modelo}"

    def actualizar_kilometraje(self, nuevo_km):
        if nuevo_km < self.kilometraje:
            print("Error: No se puede reducir el kilometraje.")
        else:
            self.kilometraje = nuevo_km

    def poner_en_venta(self):
        self.en_venta = True

    def informacion():
        pass


class Coche(Vehiculo):
    def __init__(self, marca, modelo, ano, kilometraje, en_venta, num_puertas):
        super().__init__(marca, modelo, ano, kilometraje, en_venta)
        self.num_puertas = num_puertas

    def informacion(self):
        estado_venta = "En venta" if self.en_venta else "No está en venta"
        return f"{self.marca} {self.modelo} ({self.ano}) - {self.kilometraje} km - {estado_venta}"

    def desperfecto(self):
        pass


class Moto(Vehiculo):
    def __init__(self, marca, modelo, ano, kilometraje, en_venta, tipo):
        super().__init__(marca, modelo, ano, kilometraje, en_venta)
        self.tipo = tipo

    def informacion(self):
        estado_venta = "En venta" if self.en_venta else "No está en venta"
        return f"{self.marca} {self.modelo} ({self.ano}) - {self.kilometraje} km - {estado_venta}, {self.tipo}"

    def comprobar_tipo(self, tipo):
        return self.tipo == tipo


if __name__ == "__main__":
    print(Coche("toyota", "corola", 2020, 23125, True, 4).informacion())
    print(Moto("Yamaha", "MT-07", 2019, 15000, False, "Deportiva").informacion())
    coche = Coche("Ford", "Fiesta", 2018, 30000, False, 5)
    print(coche.informacion())
    coche.poner_en_venta()
    print(coche.informacion())
    moto = Moto("Honda", "CBR600RR", 2021, 5000, True, "Deportiva")
    print(moto.informacion())
    print(moto.comprobar_tipo("Deportiva"))
    print(moto.comprobar_tipo("Scooter"))

# # reactores-> continuos
#     pfr
#     sstr
# # reactores-> descontinuos
# batch
# reactores
#     continuos
#         pfr
#         cstr
#     descontinuos
#         batch
#         semi-batch
# separacion
#     columnas
#     membranas
#         nano
#         ultra
# bombas
#     centrifuga
#     axial
# separacion
#     columnas
#     membranas
#         nano
#         ultra
#     decantadores
#         manolo
