def soma_bignum(s1, s2, i=0, vaium=0):
    if i >= len(s1) and i >= len(s2):
        if vaium == 0:
            return ""
        else:
            return str(vaium)
    if i < len(s1):
        d1 = int(s1[i])
    else:
        d1 = 0
    if i < len(s2):
        d2 = int(s2[i])
    else:
        d2 = 0
    soma = d1 + d2 + vaium
    digito = soma % 10
    novo_vaium = soma // 10
    return str(digito) + soma_bignum(s1, s2, i + 1, novo_vaium)