n,k=map(int,input().split())
x=list(map(int,input().split()))

soma=0
inicio=0
cont=0

for c in range(n):
    soma+=x[c]
    while soma>k and inicio<=c:
        soma-=x[inicio]
        inicio+=1
    if soma==k:
        cont+=1
print(cont)
