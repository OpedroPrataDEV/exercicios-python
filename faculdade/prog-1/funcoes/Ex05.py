
def minimo (vetor):
    indice=int(input('índice K: '))
    menor=vetor[indice]
    for i in range(indice,len(vetor)):
        if vetor[i]<menor:
            menor=vetor[i]
    print(menor)


minimo([6,2,9,4,6,11,2,3])

