class Hotel:
    def __init__(self, nombre, ubicacion, numero_habitaciones):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.numero_habitaciones = numero_habitaciones
        self.habitaciones_disponibles = numero_habitaciones

    def registrar_huesped(self, numero_habitaciones):
        if numero_habitaciones <= self.habitaciones_disponibles:
            self.habitaciones_disponibles -= numero_habitaciones
            print(f"{numero_habitaciones} habitaciones registradas con éxito.")
        else:
            print("No hay suficientes habitaciones disponibles.")

    def liberar_habitaciones(self, numero_habitaciones):
        self.habitaciones_disponibles += numero_habitaciones
        if self.habitaciones_disponibles > self.numero_habitaciones:
            self.habitaciones_disponibles = self.numero_habitaciones
        print(f"{numero_habitaciones} habitaciones liberadas con éxito.")

    def mostrar_informacion(self):
        print(f"Hotel: {self.nombre}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Habitaciones totales: {self.numero_habitaciones}")
        print(f"Habitaciones disponibles: {self.habitaciones_disponibles}")


# Ejemplo de uso
if __name__ == "__main__":
    hotel = Hotel("Hotel Central", "Ciudad Central", 50)
    hotel.mostrar_informacion()
    hotel.registrar_huesped(10)
    hotel.mostrar_informacion()
    hotel.liberar_habitaciones(5)
    hotel.mostrar_informacion()