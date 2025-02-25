```mermaid 
classDiagram
    class Vehiculo {
        - string marca
        - string modelo
        - int año
        - float kilometraje
        - bool en_venta
        + actualizar_kilometraje(float nuevo_km) void
        + poner_en_venta() void
        + informacion() string
    }

    class Coche {
        - int num_puertas
        + informacion() string
    }

    class Moto {
        - string tipo
        + informacion() string
    }

    Coche --|> Vehiculo : hereda
    Moto --|> Vehiculo : hereda
