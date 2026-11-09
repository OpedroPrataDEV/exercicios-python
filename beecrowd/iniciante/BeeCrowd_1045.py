valores=list(map(float,input().split()))
for c in range(len(valores)):
    for i in range(len(valores)-c-1):
        if valores[i]<valores[i+1]:
            valores[i],valores[i+1]=valores[i+1],valores[i]
a=valores[0]
b=valores[1]
c=valores[2]

if a>=b+c:
    print('NAO FORMA TRIANGULO')
elif (a**2)==(b**2)+(c**2):
    print('TRIANGULO RETANGULO')
    if a==b==c:
        print('TRIANGULO EQUILATERO')
    elif a==b!=c or a==c!=b or c==b!=a:
        print('TRIANGULO ISOSCELES')
elif (a**2)>(b**2)+(c**2):
    print('TRIANGULO OBTUSANGULO')
    if a==b==c:
        print('TRIANGULO EQUILATERO')
    elif a==b!=c or a==c!=b or c==b!=a:
        print('TRIANGULO ISOSCELES')
elif (a**2)<(b**2)+(c**2):
    print('TRIANGULO ACUTANGULO')
    if a==b==c:
        print('TRIANGULO EQUILATERO')
    elif a==b!=c or a==c!=b or c==b!=a:
        print('TRIANGULO ISOSCELES')
