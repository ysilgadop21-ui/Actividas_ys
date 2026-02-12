estudiantes = []

def agregar_estudiante(nombre, nota):
    estudiante = {"nombre": nombre, "nota": nota}
    estudiantes.append(estudiante)

def mostrar_estudiantes():
    print("\nLista de estudiantes:")
    for e in estudiantes:
        print(f"{e['nombre']} - Nota: {e['nota']}")

def calcular_promedio():
    if len(estudiantes) == 0:
        return 0
    total = sum(e["nota"] for e in estudiantes)
    return total / len(estudiantes)


# Prueba del programa
agregar_estudiante("Brayan Ortiz", 2.5)
agregar_estudiante("Gabriela Torres", 4.5)
agregar_estudiante("Sara Conde", 3.1)

mostrar_estudiantes()
print("Promedio general:", calcular_promedio())