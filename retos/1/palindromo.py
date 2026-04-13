def es_palindromo(palabra):
    izquierda = 0
    derecha = len(palabra) - 1

    while izquierda < derecha:
        if palabra[izquierda] != palabra[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True