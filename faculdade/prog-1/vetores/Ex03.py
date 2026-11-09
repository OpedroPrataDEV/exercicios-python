numeros=input('Quais Números você deseja na lista? ').split()
lista=[]
for n in numeros:
    lista.append(int(n))

lista_invertida=lista[::-1]

def fatorial_lista(x):
    if x==1 or x==0:
        return 1
    elif x<0:
        return x
    resultado=1
    for i in range(1,x+1):
        resultado=resultado*i
    return resultado

lista2=[]
for v in lista_invertida:
    lista2.append(fatorial_lista(v))
print(lista2)