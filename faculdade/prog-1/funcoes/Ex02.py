
def medidor(vetor):
    contador = 1
    maior=1
    for v in range(len(vetor) - 1):
        if vetor[v] < vetor[v + 1]:
            contador += 1
            if contador>maior:
                maior=contador
        else:
            contador=1
    return maior


print(medidor([1,2,3,1,2,3,4,1]))
