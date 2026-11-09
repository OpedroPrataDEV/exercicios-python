valor=float(input())
if 0<=valor<=2000:
    print('Isento')
elif 2000<valor<=3000:
    imposto=(valor-2000)*0.08
    print(f'R$ {imposto:.2f}')
elif 3000<valor<=4500:
    imposto=80+(valor-3000)*0.18
    print(f'R$ {imposto:.2f}')
else:
    imposto=350+(valor-4500)*0.28
    print(f'R$ {imposto:.2f}')
