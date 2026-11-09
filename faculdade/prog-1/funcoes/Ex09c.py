def media(a, b, c):
    return (a + b + c) / 3


def suavizar(f, lista):
    resultado = []
    resultado.append(lista[0])
    for i in range(1, len(lista)-1):
        valor = f(lista[i-1], lista[i], lista[i+1])
        resultado.append(valor)
    resultado.append(lista[-1])
    return resultado