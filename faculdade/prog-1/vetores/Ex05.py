from random import randint
lista1=[]
lista2=[]
lista_final=[]
for c in range(6):
    lista1.append(randint(1,10))
for c in range(4):
    lista2.append(randint(1,10))
maior=0
if len(lista1)>len(lista2):
    maior=lista1
    menor=lista2
else:
    maior=lista2
    menor=lista1
for i in range(len(menor)):
    lista_final.append(menor[i])
    lista_final.append(maior[i])
sobra=maior[len(menor):]
lista_final.extend(sobra)
print(lista1)
print(lista2)
print(lista_final)

