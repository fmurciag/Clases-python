# Juego de Adivinanzas

Descripción: Escribe un programa que  pida al usuario un numero y si es el numero no es primo que te solicite otro .

Adjunto una funcion `es_primo(numero)`para saber si es primo o no, si es primo devuelve verdadero


```Python

def es_primo(num):
    def es_primo_aux(num, n=2):
        if n >= num:
            return True
        elif num % n != 0:
            return es_primo_aux(num, n + 1)
        else:
            return False
    return es_primo_aux(num, n=2)

es_primo(13)
>> True
es_primo(2)
>> False
