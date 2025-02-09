import random
from time import sleep


def jugar():
    while True:
        print("Seleccione: [1] piedra [2] papel [3] tijera [4] lagarto [5] spock [0] salir")
        jugador = int(input("Seleccione una opción: "))
        if jugador == 0:
            print("Juego terminado.")
            break
        # Generamos la opción de la máquina de forma aleatoria
        maquina = random.randint(1, 5)
        print("Jugador elige", jugador, "- Máquina elige", maquina)
        sleep(1)  # Esperamos 1 segundo antes de mostrar el resultado para darle más emoción al juego
        if jugador == maquina:
            print("Empate")
        # condiciones si el jugador gana
        # piedra gana a tijera y lagarto,
        # papel gana a piedra y spock,
        # tijera gana a papel y lagarto,
        # lagarto gana a spock y papel,
        # spock gana a piedra y tijera
        elif (
            (jugador == 1 and (maquina == 3 or maquina == 4))
            or (jugador == 2 and (maquina == 1 or maquina == 5))
            or (jugador == 3 and (maquina == 2 or maquina == 4))
            or (jugador == 4 and (maquina == 2 or maquina == 5))
            or (jugador == 5 and (maquina == 1 or maquina == 3))
        ):
            print("Jugador gana")
        else:
            print("Máquina gana")
        print("\n")  # Salto de línea


# Iniciar el juego
jugar()
