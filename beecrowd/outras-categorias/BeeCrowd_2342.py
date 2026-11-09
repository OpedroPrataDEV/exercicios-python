max=int(input())
linha=input().split()
n1=int(linha[0])
cont=(linha[1])
n2=int(linha[2])
if cont=='+':
    if n1+n2>max:
        print('OVERFLOW')
    else:
        print('OK')
elif cont=='*':
    if n1*n2>max:
        print('OVERFLOW')
    else:
        print('OK')