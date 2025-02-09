def cambio_monedas(cantidad):
    monedas = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    resultado = {}

    for moneda in monedas:
        if cantidad >= moneda:
            # División entera para saber cuantas monedas de esa cantidad podemos dar
            cantidad_monedas = int(cantidad // moneda)
            # Restamos la cantidad de monedas * el valor de la moneda actual a la cantidad total
            # para ver cuantas monedas quedan por devolver
            cantidad -= cantidad_monedas * moneda
            # Evitar errores de punto flotante en Python (0.1 + 0.2 != 0.3)
            cantidad = round(cantidad, 2)
            # Añadimos al diccionario el valor de la moneda y la cantidad de monedas key:moneda value:cantidad_monedas
            resultado[moneda] = cantidad_monedas

    # Recorremos el diccionario para mostrar el resultado por pantalla
    for moneda, cantidad in resultado.items():
        print(f"{cantidad} moneda(s) de {moneda}€")


if __name__ == "__main__":
    while True:
        try:
            # Pedimos al usuario que introduzca una cantidad en euros y llamamos a la función cambio_monedas
            entrada = float(input("Introduce una cantidad en euros (Ctrl+C para salir): "))
            print(f"Cambio para {entrada}€:")
            cambio_monedas(entrada)

        except KeyboardInterrupt:
            # Manejamos las excepciones de KeyboardInterrupt para salir del programa con Ctrl+C
            print("\nPrograma terminado.")
            break
        except ValueError:
            # Manejamos las excepciones de ValueError para evitar que el programa termine si el usuario introduce un valor no numérico
            print("Por favor, introduce un número válido.")
