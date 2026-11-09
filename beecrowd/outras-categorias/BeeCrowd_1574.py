teste=int(input())
for c in range(teste):
    historico = []
    instruções=int(input())
    posiçao=0
    for i in range(instruções):
        movimento=input().split()
        if movimento[0]=='LEFT':
            valor_do_passo=-1
        elif movimento[0]=='RIGHT':
            valor_do_passo=1
        else:
            indice=int(movimento[2])-1
            valor_do_passo=historico[indice]
        posiçao=posiçao+valor_do_passo
        historico.append(valor_do_passo)
    print(posiçao)

