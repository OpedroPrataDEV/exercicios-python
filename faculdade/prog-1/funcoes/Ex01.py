def soma(a,b):
    calculo=a+b
    return calculo


def sub(a,b):
    calculo=a-b
    return calculo


def mult(a,b):
    calculo=a*b
    return calculo


def div(a,b):
    calculo=a/b
    return calculo

def interface_calculadora():
    n1=float(input('Primeiro número: '))
    n2=float(input('Segundo número: '))
    print('Opções disponíveis:'
          '[+]'
          '[-]'
          '[X]'
          '[D]')
    escolha=input('Sua escolha: ')

    if escolha=='+':
        resultado=(soma(n1,n2))
        print(resultado)
    elif escolha=='-':
        resultado=(sub(n1,n2))
        print(resultado)
    elif escolha=='X':
        resultado=(mult(n1,n2))
        print(resultado)
    elif escolha=='D':
        resultado=(div(n1,n2))
        print(resultado)
interface_calculadora()