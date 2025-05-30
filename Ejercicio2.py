def ordenar_por_edad(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][1] > lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


personas = [("Juan", 25), ("María", 30), ("Carlos", 20)]
ordenadas = ordenar_por_edad(personas)
print("Ordenadas por edad:", ordenadas)
