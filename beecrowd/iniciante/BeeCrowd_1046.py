n1,n2=map(int,input().split())
if n1>=n2:
    print(f'O JOGO DUROU {24-(n1-n2)} HORA(S)')
else:
    horas=abs(n1-n2)
    print(f'O JOGO DUROU {horas} HORA(S)')