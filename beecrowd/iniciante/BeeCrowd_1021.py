n=float(input())
n=n*100
nota100=nota50=nota20=nota10=nota5=nota2=moeda1=moeda50=moeda25=moeda10=moeda5=moeda01=0
nota100=n//10000
n=n%10000
nota50=n//5000
n=n%5000
nota20=n//2000
n=n%2000
nota10=n//1000
n=n%1000
nota5=n//500
n=n%500
nota2=n//200
n=n%200
moeda1=n//100
n=n%100
moeda50=n//50
n=n%50
moeda25=n//25
n=n%25
moeda10=n//10
n=n%10
moeda5=n//5
n=n%5
moeda01=n//1

print('NOTAS:')
print(f'{nota100:.0f} nota(s) de R$ 100.00')
print(f'{nota50:.0f} nota(s) de R$ 50.00')
print(f'{nota20:.0f} nota(s) de R$ 20.00')
print(f'{nota10:.0f} nota(s) de R$ 10.00')
print(f'{nota5:.0f} nota(s) de R$ 5.00')
print(f'{nota2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda1:.0f} moeda(s) de R$ 1.00')
print(f'{moeda50:.0f} moeda(s) de R$ 0.50')
print(f'{moeda25:.0f} moeda(s) de R$ 0.25')
print(f'{moeda10:.0f} moeda(s) de R$ 0.10')
print(f'{moeda5:.0f} moeda(s) de R$ 0.05')
print(f'{moeda01:.0f} moeda(s) de R$ 0.01')
