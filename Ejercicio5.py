def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

cadena = "hola mundo hola hola mundo mundo hola"
resultado = contar_palabras(cadena)
print("Conteo de palabras:", resultado)
