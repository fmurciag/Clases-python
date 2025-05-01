

def nombre(n):
    if n < 2:
        return False  # No es primo si es menor que 2
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Si encontramos un divisor, no es primo
            return False
    return True  # Si no encontramos divisores, es primo

# Bucle principal
while True:
    numero = int(input("Introduzca un número: "))
    if nombre(numero):
        print("El número es primo")
        break  # Salimos si encontramos un primo
    else:
        print("El número no es primo. Inténtalo de nuevo.")

