# Máquina de Juego: Piedra, Papel, Tijera, Lagarto, Spock

## Descripción
Crear un programa en Python que permita jugar al clásico juego *Piedra, Papel, Tijera, Lagarto, Spock* contra una máquina. El programa debe ejecutarse de forma indefinida hasta que el usuario elija salir.

## Reglas del Juego
El juego sigue estas reglas:

- **Piedra aplasta Tijera**
- **Piedra aplasta Lagarto**
- **Papel cubre Piedra**
- **Papel desautoriza Spock**
- **Tijera corta Papel**
- **Tijera decapita Lagarto**
- **Lagarto devora Papel**
- **Lagarto envenena Spock**
- **Spock vaporiza Piedra**
- **Spock rompe Tijera**

## Instrucciones
1. El usuario debe seleccionar una opción:
   - `[1] Piedra`
   - `[2] Papel`
   - `[3] Tijera`
   - `[4] Lagarto`
   - `[5] Spock`
   - `[0] Salir`
2. La máquina elegirá una opción de manera aleatoria.
   - usa numeros aleatorios [pista](https://ellibrodepython.com/numeros-aleatorios-python)
3. Se determinará el resultado según las reglas del juego.
4. El juego continuará hasta que el usuario introduzca `0` para salir.

## Ejemplo de Ejecución
