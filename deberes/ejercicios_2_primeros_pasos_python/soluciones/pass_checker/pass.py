import hashlib


def hashear_contraseña(contraseña: str) -> str:
    """hashear_contraseña con SHA-256
    Args:
        contraseña (str): Contraseña a hashear

    Returns:
        str: Contraseña hasheada con SHA-256
    """
    return hashlib.sha256(contraseña.encode()).hexdigest()


# Registro de contraseña
print("Registro de usuario")
password = input("Crea tu contraseña: ")
hashed_password = hashear_contraseña(password)  # Guardamos la contraseña hasheada

# Verificación de contraseña con intentos
intentos = 3

print("\nInicio de sesión")
# Mientras haya intentos, pedimos la contraseña
while intentos > 0:
    intento = input("Introduce tu contraseña: ")

    if hashear_contraseña(intento) == hashed_password:  # Comparamos hashes
        print("Acceso concedido")
        break
    else:
        # Si la contraseña es incorrecta, restamos un intento
        intentos -= 1
        # Si quedan intentos, mostramos un mensaje con los intentos restantes
        if intentos > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
        else:
            print("Cuenta bloqueada. Demasiados intentos fallidos.")
