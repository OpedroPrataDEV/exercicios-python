from math import sqrt
a,b,c=map(float,input().split())
delta=((b**2)-4*a*c)
if delta<0 or 2*a==0:
    print('Impossivel calcular')
else:
    r1=((b*-1)+sqrt(delta))/(2*a)
    r2=((b*-1)-sqrt(delta))/(2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
