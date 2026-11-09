r=int(input(),16)
g=int(input(),16)
b=int(input(),16)

total_verdes=(r//g)
green=total_verdes**2

total_azul=(g//b)
blue=total_azul**2

total=1+green+(blue*green)

resultado=hex(total)

print(resultado[2:])