def draw_rectangle(N, H):
    for _ in range(H):
        print("*" * N)  # mulitplica el * n veces


# Solicitar dimensiones al usuario
N = int(input("Introduce el ancho (N): "))
H = int(input("Introduce la altura (H): "))

draw_rectangle(N, H)
