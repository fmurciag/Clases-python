# 🏆 Ejercicio: El Canizador 🏆  

## 📌 Descripción  
Tu tarea es crear un **"Canizador"**, un programa que transforme una frase normal en una con estilo **"cani"**.  
Para ello, deberás aplicar ciertas reglas que modifiquen el texto introducido por el usuario.

---

## 🎯 Requisitos del programa  

1️⃣ **Entrada del usuario:**  
   - El programa pedirá al usuario que ingrese una frase.  
   
2️⃣ **Transformaciones que debe aplicar:**  
   - **Cambio de letras:**  
     - Sustituir **"c"** por **"k"** y **"qu"** por **"k"**.  
     - Reemplazar **"z"** por **"s"** para darle más estilo.  
   - **Sustituciones de palabras:**  
     - Cambiar palabras comunes por su equivalente en jerga "cani".  
     - Ejemplo: `"amigo"` → `"illo"`, `"dinero"` → `"panoja"`, `"coche"` → `"buga"`.  
   - **Repetición aleatoria de letras(opcional):**  
     - Algunas letras se repetirán aleatoriamente para darle más "flow".  
     - Ejemplo: `"loko"` → `"lokooo"`, `"vale"` → `"weno"`  
 
## Pistas
- usa `.replace("a","b")` para remplazar caracteres de una cadena de texto
- usa `.split()` para separar las palabras de una frase en una lista
- usa las posiciones de la lista
- usa `.join` para unir listas de strings en una sola
---

## 📝 Diccionario de Jerga "Cani" (Formato JSON)  

```json
{
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
    "grande": "toh basto"
}
```
## Ejemplo

```
Escribe una frase para canizar: tengo el coche en el taller, mi mujer lo recojerá

Tengo el buga en el taller, mi pibita lo rekojerá 😂🔥