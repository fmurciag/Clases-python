```mermaid 
classDiagram
    class Reactor {
        +float volumen
        +float temperatura
        +float presion
        +simular()
        +calcular_conversion(reaccion)
        +calcular_energia_reaccion(entalpia_reaccion, cantidad_reactivo)
    }

    class Continuo {
        +float caudalEntrada
        +float caudalSalida
        +simular()
        +calcular_tiempo_residencia()
        +calcular_eficiencia_termodinamica(energia_utilizada, energia_total)
    }

    class PFR {
        +float longitud
        +float diametro
        +simular()
        +calcular_perdida_carga()
        +determinar_rendimiento_reactor(conversion, selectividad)
    }

    class CSTR {
        +float agitacion
        +simular()
        +calcular_eficiencia_mezcla()
    }

    class Descontinuo {
        +float tiempoReaccion
        +simular()
        +determinar_fin_reaccion()
    }

    class Batch {
        +float cargaInicial
        +simular()
        +controlar_temperatura()
    }

    class SemiBatch {
        +float tasaAlimentacion
        +simular()
        +ajustar_alimentacion()
    }

    class Separacion {
        +float eficiencia
        +simular()
        +determinar_pureza()
        +calcular_coste_operativo(energia_consumida, costo_energia)
    }

    class Columnas {
        +int numeroPlatos
        +float altura
        +simular()
        +calcular_reflujo()
        +estimar_capacidad_produccion(flujo_alimentacion, eficiencia_separacion)
    }

    class Membranas {
        +float area
        +float presionOperacion
        +simular()
        +calcular_flujo_transmembrana()
    }

    class Nano {
        +float tamanioPoros
        +simular()
    }

    class Ultra {
        +float tamanioPoros
        +simular()
    }

    class Bombas {
        +float potencia
        +float eficiencia
        +simular()
        +calcular_flujo()
    }

    class Centrifuga {
        +float velocidadRotacion
        +simular()
        +calcular_presion_salida()
    }

    class Axial {
        +float anguloAspas
        +simular()
        +calcular_direccion_flujo()
    }

    Reactor <|-- Continuo
    Continuo <|-- PFR
    Continuo <|-- CSTR
    Reactor <|-- Descontinuo
    Descontinuo <|-- Batch
    Descontinuo <|-- SemiBatch

    Separacion <|-- Columnas
    Separacion <|-- Membranas
    Membranas <|-- Nano
    Membranas <|-- Ultra

    Bombas <|-- Centrifuga
    Bombas <|-- Axial
