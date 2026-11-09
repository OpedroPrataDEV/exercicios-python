n,m=map(int,input().split())
carros=[]
for c in range(n):
    voltas=list(map(int,input().split()))
    total=sum(voltas)
    carros.append((total,c+1))
carros.sort()
print(carros[0][1])
print(carros[1][1])
print(carros[2][1])