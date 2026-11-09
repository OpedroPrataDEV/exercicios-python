n,m=map(int,input().split())
p=list(map(int,input().split()))

p.append(42195)
resultado='S'
for i in range(len(p)-1):
    distancia=p[i+1]-p[i]
    if distancia>m:
        resultado='N'
        break
print(resultado)