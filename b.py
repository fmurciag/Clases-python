import os


def buscar_json(directorio):
    archivos_json = []
    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(".json"):
                archivos_json.append(os.path.join(raiz, archivo))
    return archivos_json


# Cambia 'ruta_del_directorio' por el directorio donde quieres buscar
ruta_del_directorio = "."  # Directorio actual
archivos_encontrados = buscar_json(ruta_del_directorio)

print("Archivos JSON encontrados:")
for archivo in archivos_encontrados:
    print(archivo)
