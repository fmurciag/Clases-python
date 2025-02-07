# 🔐 Ejercicio: Gestor de Contraseñas Seguras 🔐  

## 📌 Descripción  
En este ejercicio, crearás un **gestor de contraseñas** que permita a un usuario:  
1️⃣ **Registrar una contraseña de forma segura**  
2️⃣ **Iniciar sesión ingresando la contraseña correcta**  
3️⃣ **Bloquear el acceso tras 3 intentos fallidos**  

Sin embargo, **no podemos guardar la contraseña en texto plano**, ya que sería un gran riesgo de seguridad. En su lugar, la convertiremos en un **hash** utilizando `sha256`.  

---

## 🔍 ¿Qué es el Hashing y por qué se usa?  
El **hashing** es un proceso que transforma una cadena de texto en una secuencia de caracteres irreversibles. Esto significa que **no se puede recuperar la contraseña original a partir del hash**, lo que la hace más segura en caso de que los datos sean comprometidos.  

En este ejercicio, usaremos el algoritmo **SHA-256** de la biblioteca estándar de Python (`hashlib`).  

### 📌 ¿Cómo convertir una contraseña en un hash?  
Podemos usar el siguiente código en Python para hashear una contraseña:  

```python
import hashlib

contraseña = "miClaveSecreta123"
hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

print(hash_contraseña)
```

## 🎯 Requisitos del programa  

### 🔹 **Registro de usuario:**  
✅ Pedir al usuario que ingrese una contraseña.  
✅ Hashear la contraseña usando `hashlib.sha256()` antes de almacenarla.  

### 🔹 **Inicio de sesión:**  
✅ Pedir al usuario que introduzca su contraseña.  
✅ Comparar el **hash** de la contraseña ingresada con el hash almacenado.  
✅ Si coincide, mostrar `✅ Acceso concedido`.  
✅ Si no coincide, permitir **hasta 3 intentos** antes de bloquear el acceso.  

---

## 📝 Ejemplo de ejecución  
```
Registro de usuario
Crea tu contraseña: 1234

Inicio de sesión
Introduce tu contraseña: 45566
Contraseña incorrecta. Te quedan 2 intentos.
Introduce tu contraseña: 3456
Contraseña incorrecta. Te quedan 1 intentos.
Introduce tu contraseña: 22
Cuenta bloqueada. Demasiados intentos fallidos.

```




