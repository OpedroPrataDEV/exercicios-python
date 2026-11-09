from random import randint
lista=[]
for c in range(100):
    lista.append(randint(1,100))
escolha=int(input('Qual valor você deseja conferir? '))
for i,v in enumerate(lista):
    if v==escolha:
        print(f'O Número {escolha} aparece em {i}')