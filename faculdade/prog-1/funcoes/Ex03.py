from random import randint
def subst(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i]=0
        elif vetor[i] < 10:
            vetor[i]=1
        else:
            vetor[i]=2
    return vetor


lista=[]
for c in range(20):
    lista.append(randint(-50,50))
print(lista)
print(subst(lista))



