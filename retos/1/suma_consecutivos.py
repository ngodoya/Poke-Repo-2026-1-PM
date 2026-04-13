def mayor_suma_consecutivos(lista):
    if len(lista) < 2:
        return None

    max_suma = lista[0] + lista[1]

    for i in range(len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > max_suma:
            max_suma = suma

    return max_suma