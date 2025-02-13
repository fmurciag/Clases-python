# Análisis de Calificaciones
Dado un diccionario donde las claves son nombres de estudiantes y los valores son listas de calificaciones, crea una función que devuelva un nuevo diccionario con los promedios de cada estudiante.

```python
alumnos = {
    "María": [8, 9, 10],
    "Carlos": [5, 6, 7],
    "Laura": [9, 9, 10]
}

print(calcular_promedios(alumnos))
# Salida: {'María': 9.0, 'Carlos': 6.0, 'Laura': 9.33}
