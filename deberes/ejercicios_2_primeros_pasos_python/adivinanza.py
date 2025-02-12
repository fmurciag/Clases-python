def es_primo(num:int):
    def es_primo_aux(num, n=2):
        if n >= num:
            print("Enhorabuena, tu número es primo.")
            return True
        elif num % n != 0:
            return es_primo_aux(num, n + 1)
        else:
            print("Tu número no es primo, prueba con otro.")
            return False
    return es_primo_aux(num, n=2)


while True:
    number = input("Insertar un número : ")
    if number == "cerrar":
        break
    elif es_primo(int(number)) == True:
        break
    else:
        continue