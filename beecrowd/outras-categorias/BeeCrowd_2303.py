l,c,m,n=map(int,input().split())
matriz=[]
for i in range(l):
    matriz.append(list(map(int,input().split())))
maior=0
for r in range(0,l,m):
    for x in range(0,c,n):
        soma=0
        for i in range(r,r+m):
            for j in range(x,x+n):
                soma+=matriz[i][j]

        if soma>maior:
            maior=soma
print(maior)
