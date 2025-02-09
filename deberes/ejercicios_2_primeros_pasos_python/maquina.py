#Máquina de cambio de monedas

def cambio_monedas(perras:float):
    lista_monedas=[2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    for i in range(0, len(lista_monedas)):
        moneda_seleccionada = lista_monedas[i]
        resultado = perras / moneda_seleccionada
        cociente = perras // moneda_seleccionada
        resto = round(perras % moneda_seleccionada,4)
        if cociente < 1:
            perras = resto

        elif cociente > 1:
            print(f"{cociente} monedas de {moneda_seleccionada} euros")
            perras = resto
            continue
        else:
            print(f"{cociente} moneda de {moneda_seleccionada} euros")
            perras = resto
            continue

salir = False
while not salir:
    number = input("Insertar una cantidad de perras :")
3.68    if number == "cerrar":
        salir = True
    else:
        number_ = float(number)
        cambio_monedas(number_)
