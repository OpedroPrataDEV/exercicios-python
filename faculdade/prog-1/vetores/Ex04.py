from random import randint
lista=[]
for c in range(100):
    lista.append(randint(1,100))
soma=0
for v in lista:
    soma+=v
media=soma/100
mais_proximo=lista[0]
diferença=abs(media-lista[0])
for v in lista:
    diferença_atual=abs(media-v)
    if diferença_atual<diferença:
        mais_proximo=v
        diferença=diferença_atual
print(media)
print(mais_proximo)