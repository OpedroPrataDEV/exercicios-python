testes=int(input())
for c in range(testes):
    cont=0
    alunos=int(input())
    notas=list(map(int,input().split()))
    ordenada=sorted(notas,reverse=True)
    for c in range(len(notas)):
        if notas[c]==ordenada[c]:
            cont+=1
    print(cont)
