def sumar_elementos(lista):
    suma = 0
    for elemento in lista:
        if isinstance(elemento, (int, float)):
            suma += elemento
        else:
            print(f"Advertencia: '{elemento}' no es un número y será ignorado.")
    return suma


numeros = [1, 2, 'a', 3.5, 4]
resultado = sumar_elementos(numeros)
print("La suma es:", resultado)
