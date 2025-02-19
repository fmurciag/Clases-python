def draw_sqr(Length:int,Width:int):
    for i in range(0, Length):
     print('*' * Width)


while True:
    number = input("Insertar la longitud del cuadrado :")

    if number == "cerrar":
        break

    number_ = input("Insertar la anchura del cuadrado :")

    if number_ == "cerrar":
        break
    
    else:
        Length = int(number)
        Width = int(number_)
        draw_sqr(Length, Width)
