from random import randint
lista=[]
for i in range(100):
    numero=randint(1,500)
    if len(lista)==0:
        lista.append(numero)
    else:
        for p in range(len(lista)):
            if numero < lista[p]:
                lista.insert(p,numero)
                break
        else:
            lista.append(numero)
print(lista)

