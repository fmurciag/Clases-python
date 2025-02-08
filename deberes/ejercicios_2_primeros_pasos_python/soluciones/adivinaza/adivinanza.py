def es_primo(num):
    def es_primo_aux(num, n=2):
        if num < 2:
            return False
        if n * n > num:
            return True
        if num % n == 0:
            return False
        return es_primo_aux(num, n + 1)

    return es_primo_aux(num)


def solicitar_numero_primo():
    while True:
        numero = int(input("Introduce un número primo: "))
        if es_primo(numero):
            print(f"¡Correcto! {numero} es un número primo.")
            break
        else:
            print(f"{numero} no es primo. Inténtalo de nuevo.")


solicitar_numero_primo()
