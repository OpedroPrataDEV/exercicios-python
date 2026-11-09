from random import randint
lista=[]
for c in range(500):
    lista.append(randint(1,500))
for i,v in enumerate(lista):
    if v%10==0:
        gratuidades=v//10
        print(f'O cliente {i} tem direito a {gratuidades} gratuidades')