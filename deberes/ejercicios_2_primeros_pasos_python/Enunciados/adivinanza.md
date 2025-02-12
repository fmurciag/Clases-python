# Juego de Adivinanzas

Descripción: Escribe un programa que pida al usuario un número y si es el número no es primo que te solicite otro.

Adjunto una función `es_primo(número)` para saber si es primo o no, si es primo devuelve verdadero.

---
```python

def es_primo(num):
    def es_primo_aux(num, n=2):
        if n >= num:
            return True
        elif num % n != 0:
            return es_primo_aux(num, n + 1)
        else:
            return False
    return es_primo_aux(num, n=2)
```
---
`es_primo(13)`

-> True

`es_primo(4)`

-> False
