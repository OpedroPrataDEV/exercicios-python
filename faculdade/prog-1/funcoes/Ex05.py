
def minimo (vetor):
    indice=int(input('índice K: '))
    menor=999
    for i in range(vetor[indice],len(vetor)-1):
        if i<menor:
            menor=i
    print(i)


minimo([6,2,9,4,6,11,2,3])

