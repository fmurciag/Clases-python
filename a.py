"""todo:
- Carga el JSON en Python. +
- Filtra solo los usuarios que están activos (activo: true). +
- Ordena los usuarios activos por edad de menor a mayor.
- Imprime los nombres y edades de los usuarios activos ordenados.
"""

import pprint
import json

USUARIOS = json.load(open("data.json"))

users_activos = []
for usuario in USUARIOS:
    if usuario["activo"]:
        users_activos.append(usuario)
print(users_activos)
# ordenar por edad
print()
print()
print()
# recorro los elemnos de usuarios activos
# ordenar esa iteracion
usuarios_ordenados = []
users_activos_copy = users_activos.copy()

for _ in range(len(users_activos_copy)):
    menor = users_activos_copy[0]
    for usuario in users_activos_copy:
        if usuario["edad"] < menor["edad"]:
            menor = usuario

    usuarios_ordenados.append(menor)
    users_activos_copy.remove(menor)

pprint.pprint(usuarios_ordenados)
