def crear_asignatura():
    asignatura = {
        "codasig": input("Código de asignatura: "),
        "nomasig": input("Nombre de la asignatura: "),
        "programa": input("Programa al que pertenece: "),
        "facultad": input("Facultad: "),
        "estudiantes": []
    }

    cantidad = int(input("¿Cuántos estudiantes desea ingresar?: "))
    for i in range(cantidad):
        print(f"\nEstudiante {i+1}:")
        codigo = input("  Código: ")
        nombres = input("  Nombres: ")
        apellidos = input("  Apellidos: ")
        definitiva = float(input("  Nota definitiva: "))

        estudiante = {
            "codigo": codigo,
            "nombres": nombres,
            "apellidos": apellidos,
            "def": definitiva
        }

        asignatura["estudiantes"].append(estudiante)

    return asignatura


def ordenar_por_nota(estudiantes):
    # Ordenamiento manual tipo burbuja (de mayor a menor)
    n = len(estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estudiantes[j]["def"] < estudiantes[j + 1]["def"]:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]
    return estudiantes


def mostrar_resultados(asignatura):
    print("\n--- Resultados ordenados por nota definitiva (de mayor a menor) ---")
    estudiantes_ordenados = ordenar_por_nota(asignatura["estudiantes"])

    for est in estudiantes_ordenados:
        print(f"{est['nombres']} {est['apellidos']} - Promedio: {est['def']}")


# Ejecución principal del programa
asignatura = crear_asignatura()
mostrar_resultados(asignatura)