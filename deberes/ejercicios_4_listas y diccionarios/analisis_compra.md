# Analizar Productos de la compra 
vamos a crear un programa que reciba información de productos de compra y que los analice lo haremos por apartados
## 1 calcular costo total
Crea una función que reciba información de productos como argumentos variables

Cada producto tiene un precio y una cantidad. La función debe calcular y devolver:
- El costo total de cada producto (precio * cantidad).
- El costo total de la compra.

> [!TIP]
> usa **kwargs

## ejemplo
```Python
compra = calcular_total_compra(
    manzanas={"precio": 1.5, "cantidad": 4},
    platanos={"precio": 0.8, "cantidad": 6},
    naranjas={"precio": 1.2, "cantidad": 3}
)

#solucion del print ejemplo:
Costos por producto: {'manzanas': 6.0, 'platanos': 4.8, 'naranjas': 3.6}
Costo total de la compra: 14.4
```
## 2 Análisis de la Compra
Ahora, crearemos una función llamada `analizar_compra` que llamará a `calcular_total_compra`. Esta nueva función debe:

- Obtener los costos de cada producto y el costo total de la compra llamando a `calcular_total_compra`.
- Identificar el producto más caro y el más barato en términos de costo total.
> [!TIP]
> Esta tiene que ser la variable resultado
> resultado = {
> "costos_por_producto": total_por_producto,
> "costo_total_compra": total_compra,
> "producto_mas_caro": producto_mas_caro,
> "producto_mas_barato": producto_mas_barato,
> "productos_ordenados": productos_ordenados_lista
>}
## Ejemplo

```python
compra = analizar_compra(
    manzanas={"precio": 1.5, "cantidad": 4},
    platanos={"precio": 0.8, "cantidad": 6},
    naranjas={"precio": 1.2, "cantidad": 3}
)

#solucion del print ejemplo:
Costos por producto: {'manzanas': 6.0, 'platanos': 4.8, 'naranjas': 3.6}
Costo total de la compra: 14.4
Producto más caro: manzanas
Producto más barato: naranjas
```


## 3 ordena la compra
Ahora, necesitamos crear una funcion que ordene los articulos de mayor a menor costo y añadri esta funcionalidad a la `analizar_compra`, **este es un apartado para pensar**
- crea una funcion que ordene sin usar las funciones e orden del sistema
- Generar una lista de productos ordenados de mayor a menor costo.

> [!WARNING]
> no nombres a la funcion `sorted()` o `sort()` ya que son funciones del sistema para ordenar

>[!Tip]
>puedes ver esta pagina [aqui](https://www.freecodecamp.org/espanol/news/algoritmos-de-ordenacion-explicados-con-ejemplos-en-javascript-python-java-y-c/) que explica algoritmos de ordenacion, esta el codigo python, intentar no mirarlo y pensar, podeis usar cualquier algoritmo, yo seria coherente y elegiria el de la burguja (bubblesort), pero si os armais de valor y quereis montar el Mergesort o el Quicksort os doy la mano (el Quicksort es sencillo)
## Ejemplo

```python
compra = analizar_compra(
    manzanas={"precio": 1.5, "cantidad": 4},
    platanos={"precio": 0.8, "cantidad": 6},
    naranjas={"precio": 1.2, "cantidad": 3}
)

#solucion del print ejemplo:
Costos por producto: {'manzanas': 6.0, 'platanos': 4.8, 'naranjas': 3.6}
Costo total de la compra: 14.4
Producto más caro: manzanas
Producto más barato: naranjas
Productos ordenados de mayor a menor costo: [{'producto': 'manzanas', 'costo_total': 6.0}, {'producto': 'platanos', 'costo_total': 4.8}, {'producto': 'naranjas', 'costo_total': 3.6}]
```


