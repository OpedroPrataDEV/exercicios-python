dados=input().split()


litro_alcool=float(dados[0])
litro_gasolina=float(dados[1])
km_alcool=float(dados[2])
km_gasolina=float(dados[3])


rendimento_alcool=km_alcool/litro_alcool
rendimento_gasolina=km_gasolina/litro_gasolina

if rendimento_gasolina<rendimento_alcool:
    print('A')
else:
    print('G')
