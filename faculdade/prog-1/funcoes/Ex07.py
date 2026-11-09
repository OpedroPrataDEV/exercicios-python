def eh_palindromo(s,inicio,fim):
    if inicio>=fim:
        return True
    if s[inicio] != s[fim]:
        return False
    return eh_palindromo(s,inicio + 1,fim - 1)


print(eh_palindromo('radar',0,len('radar')-1))