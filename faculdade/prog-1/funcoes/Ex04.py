def fracionario(numerador,denominador):
    num_atual=2
    den_atual=3
    soma=0.0
    while num_atual<=a and den_atual<=b:
        soma+=num_atual/den_atual
        num_atual+=1
        den_atual+=2
    print(f'{soma:.2f}')


a=int(input('Informe o Numerador: '))
b=int(input('Informe o Denominador: '))
if a<0:
    while a<0:
        print('Número inválido, Tente novamente...')
        a=int(input('Numerador: '))



fracionario(a,b)




