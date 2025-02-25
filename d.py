def construir_montana(lista):
    lista.sort()  # Ordenamos la lista en orden ascendente
    mayor = lista.pop()  # Extraemos el mayor
    pares = [num for num in lista if num % 2 == 0]  # Filtramos los pares
    impares = [num for num in lista if num % 2 != 0]  # Filtramos los impares

    montana = pares + [mayor] + impares  # Concatenamos los pares, el mayor y los impares
    return montana


# Ejemplo de uso
lista_original = [1, 2, 3, 4, 5, 6, 7]
montana = construir_montana(lista_original)
print(montana)
