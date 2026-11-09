n=input().split()
codigo=n[0]
qtd=int(n[1])

if codigo=='1':
    print(f'Total: R$ {qtd*4:.2f}')
elif codigo=='2':
    print(f'Total: R$ {qtd*4.5:.2f}')
elif codigo=='3':
    print(f'Total: R$ {qtd*5:.2f}')
elif codigo=='4':
    print(f'Total: R$ {qtd*2:.2f}')
elif codigo=='5':
    print(f'Total: R$ {qtd*1.5:.2f}')