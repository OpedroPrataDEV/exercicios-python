import math
a,b,c,d=map(int,input().split())
numerador_1=a
denominador_1=b
numerador_2=c
denominador_2=d

numerador_total=(numerador_1*denominador_2)+(numerador_2*denominador_1)
denomindador_total=b*d

divisor_comum=math.gcd(numerador_total,denomindador_total)
print(numerador_total//divisor_comum,denomindador_total//divisor_comum)

