def invertir_diccionario(diccionario):
    nuevo_diccionario = {}
    for clave, valor in diccionario.items():
        nuevo_diccionario[valor] = clave
    return nuevo_diccionario

original = {"a": 1, "b": 2, "c": 56}
invertido = invertir_diccionario(original)
print("Diccionario invertido:", invertido)