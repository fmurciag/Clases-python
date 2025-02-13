def calcular_total_compra(**productos):
    total_por_producto = {nombre: datos["precio"] * datos["cantidad"] for nombre, datos in productos.items()}
    total_compra = sum(total_por_producto.values())

    return total_por_producto, total_compra


def analizar_compra(**productos):
    # Llamamos a la función calcular_total_compra
    total_por_producto, total_compra = calcular_total_compra(**productos)

    # Encontrar el producto más caro y el más barato
    producto_mas_caro = max(total_por_producto, key=total_por_producto.get)
    producto_mas_barato = min(total_por_producto, key=total_por_producto.get)

    # Ordenar productos por costo total de mayor a menor
    productos_ordenados = sorted(total_por_producto.items(), key=lambda x: x[1], reverse=True)

    # Convertimos la lista de tuplas en una lista de diccionarios
    productos_ordenados_lista = [{"producto": p, "costo_total": c} for p, c in productos_ordenados]

    # Resultado final con información adicional
    resultado = {
        "costos_por_producto": total_por_producto,
        "costo_total_compra": total_compra,
        "producto_mas_caro": producto_mas_caro,
        "producto_mas_barato": producto_mas_barato,
        "productos_ordenados": productos_ordenados_lista,
    }

    return resultado


# Ejemplo de uso
compra_info = analizar_compra(
    manzanas={"precio": 1.5, "cantidad": 4},
    platanos={"precio": 0.8, "cantidad": 6},
    naranjas={"precio": 1.2, "cantidad": 3},
)

# Imprimir resultados
print("Costos por producto:", compra_info["costos_por_producto"])
print("Costo total de la compra:", compra_info["costo_total_compra"])
print("Producto más caro:", compra_info["producto_mas_caro"])
print("Producto más barato:", compra_info["producto_mas_barato"])
print("Productos ordenados de mayor a menor costo:", compra_info["productos_ordenados"])
