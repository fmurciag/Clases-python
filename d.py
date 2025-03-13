from pathlib import Path
import glob


def buscar_json(directorio):
    return list(Path(directorio).rglob("*.json"))


ruta_del_directorio = "."  # Directorio actual
archivos_encontrados = buscar_json(ruta_del_directorio)

print("Archivos JSON encontrados:")
for archivo in archivos_encontrados:
    print(archivo)
