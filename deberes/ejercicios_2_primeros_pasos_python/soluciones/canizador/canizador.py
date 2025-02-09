import random


def canizador(frase):
    # Lista de palabras canis comunes
    palabras_canis = {
        "chico": "shurmano",
        "amigo": "illo",
        "tío": "lokooo",
        "colega": "bro",
        "dinero": "panoja",
        "trabajo": "curro",
        "coche": "buga",
        "mujer": "pibita",
        "fiesta": "jolgorio",
        "cerveza": "birra",
        "vale": "weno",
        "claro": "de una",
        "sí": "zi",
        "no": "noh",
        "cómo": "komor",
        "hola": "wenaaa",
        "estoy": "toy",
        "chaval": "shava",
        "gente": "peñita",
        "fuerte": "toh wapo",
        "guapo": "wapens",
        "pequeño": "piki",
        "grande": "toh basto",
    }

    # Transformaciones de estilo "cani"
    # minúsculas
    frase = frase.lower()
    # Dividimos la frase en palabras
    palabras = frase.split()

    # Sustituciones de palabras canis
    for i in range(len(palabras)):
        # Si la palabra está en el diccionario de palabras canis la sustituimos
        if palabras[i] in palabras_canis:
            palabras[i] = palabras_canis[palabras[i]]  # Sustitución de palabras
    frase = " ".join(palabras)  # Unimos las palabras
    frase = frase.replace("c", "k").replace("qu", "k").replace("z", "s")  # Cambio de letras

    # Toques finales (emojis y alargamientos de palabras)
    frase = frase.capitalize() + " 😂🔥"

    return frase


# Prueba el canizador
frase_usuario = input("Escribe una frase para canizar: ")
print(canizador(frase_usuario))
