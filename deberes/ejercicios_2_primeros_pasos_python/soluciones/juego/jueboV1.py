import random
from time import sleep


def jugar():
    opciones = {1: "piedra", 2: "papel", 3: "tijera", 4: "lagarto", 5: "spock"}

    # Reglas del juego en forma de tuplas (jugador, maquina): resultado
    reglas_para_ganar = {
        (1, 3): "Jugador gana",
        (1, 4): "Jugador gana",
        (2, 1): "Jugador gana",
        (2, 5): "Jugador gana",
        (3, 2): "Jugador gana",
        (3, 4): "Jugador gana",
        (4, 2): "Jugador gana",
        (4, 5): "Jugador gana",
        (5, 1): "Jugador gana",
        (5, 3): "Jugador gana",
    }

    while True:
        print("Seleccione: [1] piedra [2] papel [3] tijera [4] lagarto [5] spock [0] salir")
        jugador = int(input("Seleccione una opción: "))
        if jugador == 0:
            print("Juego terminado.")
            break
        # Validamos que la opción seleccionada por el jugador sea válida
        if jugador not in opciones:
            print("Opción inválida, intenta de nuevo.")
            continue
        # Generamos la opción de la máquina de forma aleatoria
        maquina = random.randint(1, 5)
        print(f"Jugador: {opciones[jugador]} - Máquina: {opciones[maquina]}")
        sleep(1)  # Esperamos 1 segundo antes de mostrar el resultado para darle más emoción al juego

        # Comprobamos el resultado del juego
        # Si la tupla (jugador, maquina) está en el diccionario de reglas_para_ganar, el jugador gana
        # Si no está, la máquina gana o si es un empate si las opciones son iguales
        if jugador == maquina:
            print("Empate")
        elif (jugador, maquina) in reglas_para_ganar:
            print("Jugador gana")
        else:
            print("Máquina gana")
        print("\n")  # Salto de línea


if __name__ == "__main__":
    jugar()
