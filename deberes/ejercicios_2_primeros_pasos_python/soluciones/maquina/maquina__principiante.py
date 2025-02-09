def cambio_monedas(cantidad):
    resultado = {}
    # Comprobamos si la cantidad es mayor o igual a cada moneda y restamos la cantidad de monedas * el valor de la moneda
    # para saber cuantas monedas de esa cantidad podemos dar y cuantas quedan por devolver en la cantidad total
    if cantidad >= 2.00:
        resultado[2.00] = int(cantidad // 2.00)
        cantidad -= resultado[2.00] * 2.00  # guardamos la cantidad de monedas de 2€ en el diccionario
        # no es necesario guardar el resultado, se puede hacer imporimir directamente
        cantidad = round(cantidad, 2)

    # Repetimos el proceso para cada moneda en orden descendente
    # asi nos aseguramos de que se devuelvan las monedas de mayor valor primero
    if cantidad >= 1.00:
        resultado[1.00] = int(cantidad // 1.00)
        cantidad -= resultado[1.00] * 1.00
        cantidad = round(cantidad, 2)

    if cantidad >= 0.50:
        resultado[0.50] = int(cantidad // 0.50)
        cantidad -= resultado[0.50] * 0.50
        cantidad = round(cantidad, 2)

    if cantidad >= 0.20:
        resultado[0.20] = int(cantidad // 0.20)
        cantidad -= resultado[0.20] * 0.20
        cantidad = round(cantidad, 2)

    if cantidad >= 0.10:
        resultado[0.10] = int(cantidad // 0.10)
        cantidad -= resultado[0.10] * 0.10
        cantidad = round(cantidad, 2)

    if cantidad >= 0.05:
        resultado[0.05] = int(cantidad // 0.05)
        cantidad -= resultado[0.05] * 0.05
        cantidad = round(cantidad, 2)

    if cantidad >= 0.02:
        resultado[0.02] = int(cantidad // 0.02)
        cantidad -= resultado[0.02] * 0.02
        cantidad = round(cantidad, 2)

    if cantidad >= 0.01:
        resultado[0.01] = int(cantidad // 0.01)
        cantidad -= resultado[0.01] * 0.01
        cantidad = round(cantidad, 2)

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
