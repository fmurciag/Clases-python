def draw_rectangle(N, H):
    for _ in range(H):  # Bucle para las filas (altura)
        for _ in range(N):  # Bucle para las columnas (ancho)
            print("*", end="")  # Imprime un * sin salto de línea
        print()  # Salto de línea al final de cada fila


# Solicitar dimensiones al usuario
N = int(input("Introduce el ancho (N): "))
H = int(input("Introduce la altura (H): "))

draw_rectangle(N, H)
