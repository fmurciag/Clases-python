from chrem_fact.reactor.continuo.pfr import PFR

from chrem_fact.separacion.membranas.nano import Nano
from chrem_fact.separacion.separacion import Columnas
from chrem_fact.bombas.centrifuga import Centrifuga


if __name__ == "__main__":
    # Crear instancias de los objetos
    reactor1 = PFR(volumen=10, temperatura=300, presion=2, caudal_entrada=5, caudal_salida=5, longitud=5, diametro=0.5)
    reactor2 = PFR(volumen=15, temperatura=350, presion=3, caudal_entrada=7, caudal_salida=7, longitud=6, diametro=0.4)
    separador = Columnas(eficiencia=95, numero_platos=10, altura=5)
    bomba = Centrifuga(potencia=10, eficiencia=85, velocidad_rotacion=3000)

    # Iniciando el proceso de simulación
    print()
    print("Simulación del proceso de producción de polímeros")
    print()
    print("--------------------------------------------------")
    # Reactor 1 - PFR 1 - Simulación
    print("Simulación del primer reactor PFR")
    reactor1.simular()
    reactor1.calcular_perdida_carga()
    print(
        f"Energía requerida para la reacción: {reactor1.calcular_energia_reaccion(entalpia_reaccion=-100, cantidad_reactivo=2)} J"
    )
    print(f"Rendimiento del reactor: {reactor1.determinar_rendimiento_reactor(conversion=0.85, selectividad=0.9)}")
    print("--------------------------------------------------")
    print()
    # Reactor 2 - PFR 2 - Simulación
    print("Simulación del segurndo reactor PFR")
    reactor2.simular()
    reactor2.calcular_perdida_carga()
    print(
        f"Energía requerida para la reacción en el segundo PFR: {reactor2.calcular_energia_reaccion(entalpia_reaccion=-120, cantidad_reactivo=3)} J"
    )
    print(
        f"Rendimiento del segundo reactor: {reactor2.determinar_rendimiento_reactor(conversion=0.9, selectividad=0.85)}"
    )
    print("--------------------------------------------------")
    print()
    # Separador - Columna - Simulación
    print("Simulación de la columna de separación")
    separador.simular()
    separador.calcular_reflujo()
    print(
        f"Capacidad de producción estimada: {separador.estimar_capacidad_produccion(flujo_alimentacion=50, eficiencia_separacion=0.95)} kg/h"
    )
    print(f"Coste operativo: {separador.calcular_coste_operativo(energia_consumida=500, costo_energia=0.12)} €")
    print("--------------------------------------------------")
    print()
    # Bomba - Centrífuga - Simulación
    print("Simulación de la bomba centrífuga")
    bomba.simular()
    bomba.calcular_presion_salida()
    print(f"Potencia requerida: {round(bomba.calcular_potencia_requerida(caudal=10, altura=5), 3)} W")
    print("--------------------------------------------------")
    print()
