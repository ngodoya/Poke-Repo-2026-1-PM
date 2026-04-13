def mismas_letras(lista):
    resultado = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if sorted(lista[i]) == sorted(lista[j]):
                if lista[i] not in resultado:
                    resultado.append(lista[i])
                if lista[j] not in resultado:
                    resultado.append(lista[j])

    return resultado