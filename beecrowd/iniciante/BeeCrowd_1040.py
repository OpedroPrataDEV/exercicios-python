n1,n2,n3,n4=map(float,input().split())
media=((n1*2)+(n2*3)+(n3*4)+(n4))/10
if 5<=media<=6.9:
    exame=float(input())
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {exame:.1f}')
    final=(exame+media)/2
    if final>=5:
        print('Aluno aprovado.')
        print(f'Media final: {final:.1f}')
    elif final<5:
        print('Aluno reprovado.')
        print(f'Media final: {final:.1f}')
elif media>=7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media<5:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
