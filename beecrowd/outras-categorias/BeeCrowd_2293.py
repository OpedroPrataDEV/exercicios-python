#Número de Linhas e Colunas:
n,m=map(int,input().split())

#Montagem da Matriz:
campo=[]
for l in range(n):
    linha=list(map(int,input().split()))
    campo.append(linha)

maior_soma=0
for i in range(n):
    soma_linha=sum(campo[i])
    if soma_linha>maior_soma:
        maior_soma=soma_linha

for j in range(m):
    soma_coluna=0
    for i in range(n):
        soma_coluna+=campo[i][j]
    if soma_coluna>maior_soma:
        maior_soma=soma_coluna

print(maior_soma)