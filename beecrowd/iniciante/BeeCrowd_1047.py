h1,m1,h2,m2=map(int,input().split())
minutagem_incial=(h1*60)+m1
minutagem_final=(h2*60)+m2
minutagem=minutagem_final-minutagem_incial
if minutagem<=0:
    minutagem+=1440
horas=minutagem//60
minutos=minutagem%60
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')