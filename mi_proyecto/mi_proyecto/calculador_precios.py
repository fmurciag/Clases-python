def calcular_precio_final(precio_base, impuesto, descuento=0):
    """
    Calcula el precio final de un producto aplicando impuesto y descuento.

    Args:
        precio_base (float): El precio base del producto.
        impuesto (float): El porcentaje de impuesto a aplicar (en decimal, por ejemplo 0.15 para 15%).
        descuento (float, opcional): El porcentaje de descuento a aplicar (en decimal, por ejemplo 0.10 para 10%). Por defecto es 0.

    Returns:
        float: El precio final del producto.
    """
    if precio_base < 0 or impuesto < 0 or descuento < 0:
        raise ValueError("El precio base, impuesto y descuento deben ser valores no negativos.")

    precio_con_impuesto = precio_base + (precio_base * impuesto)
    precio_final = precio_con_impuesto - (precio_con_impuesto * descuento)
    return round(precio_final, 2)


# Ejemplo de uso
if __name__ == "__main__":
    precio_base = 100.0  # Precio base del producto
    impuesto = 0.15  # 15% de impuesto
    descuento = 0.10  # 10% de descuento

    precio_final = calcular_precio_final(precio_base, impuesto, descuento)
    print(f"El precio final del producto es: ${precio_final}")
