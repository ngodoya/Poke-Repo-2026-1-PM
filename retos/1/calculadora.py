def calculadora(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            return "Error: división por cero"
        return a / b
    else:
        return "Operador inválido"