personas = [
    {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
    {"nombres": "Bayron Andres", "apellidos": "Pedraza Ramirez", "edad": 55},
    {"nombres": "Juan Carlos", "apellidos": "Fernández López", "edad": 103},
    {"nombres": "Ana Sofía", "apellidos": "Rojas Gutiérrez", "edad": 45}
]

def imprimir_personas_mayores_de(personas, edad_limite):
    print(f"Personas mayores de {edad_limite} años:")
    for persona in personas:
        if persona["edad"] > edad_limite:
            print(f"{persona['nombres']} {persona['apellidos']}")

imprimir_personas_mayores_de(personas, 100)

