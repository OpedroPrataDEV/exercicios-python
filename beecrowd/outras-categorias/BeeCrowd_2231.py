teste=1
while True:
    maior=-999999
    menor=99999999
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    lista=[]
    for c in range(n):
        lista.append(int(input()))
    p=[0]*(n+1)
    for i in range(len(lista)):
        p[i+1]=p[i]+lista[i]
    for c in range(n-m+1):
        soma_atual=p[c+m]-p[c]
        media_atual=soma_atual/m
        media=int(media_atual)
        if media>maior:
            maior=media
        if media<menor:
            menor=media
    print(f'Teste {teste}')
    print(menor, maior)
    print()
    teste+=1
