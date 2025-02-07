def par(n:int):
    resto = n % 2
    if resto == 0:
        espar = True
        print("El número es par")
    else:
        espar = False
        print("El número no es par")
        print(f"El resto es : {resto}")

salir = False
while not salir:
    number = input("Insertar un numero :")
    if number == "cerrar":
        salir = True
    else:
        number_ = int(number)
        par(number_)