pinos=input().split()
qtd_pinos=int(pinos[0])
altura_desejada=int(pinos[1])


altura_atual=list(map(int,input().split()))
movimentos=0
for i in range(qtd_pinos-1):
    diferença=altura_desejada-altura_atual[i]
    movimentos+=abs(diferença)
    altura_atual[i]+=diferença
    altura_atual[i+1]+=diferença
print(movimentos)

