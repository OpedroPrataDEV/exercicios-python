qtd=int(input())
paises=[]
for c in range(qtd):
    linha=input().split()
    nome=linha[0]
    ouro=int(linha[1])
    prata=int(linha[2])
    bronze=int(linha[3])
    paises.append([nome,ouro,prata,bronze])
paises.sort(key=lambda x:x[0])
paises.sort(key=lambda x:x[3],reverse=True)
paises.sort(key=lambda x:x[2],reverse=True)
paises.sort(key=lambda x:x[1],reverse=True)

for x in paises:
    print(x[0],x[1],x[2],x[3])