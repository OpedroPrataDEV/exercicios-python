
din,op=map(int,input().split())
dalia=eloi=felix=din
for c in range(op):
    dados=input().split()
    açao=dados[0].upper()
    if açao=='C':
        pessoa = dados[1].upper()
        valor = int(dados[2])
        if pessoa=='D':
            dalia=dalia-valor
        elif pessoa=='E':
            eloi=eloi-valor
        elif pessoa=='F':
            felix=felix-valor
    elif açao=='V':
        pessoa = dados[1].upper()
        valor = int(dados[2])
        if pessoa=='D':
            dalia=dalia+valor
        elif pessoa=='E':
            eloi=eloi+valor
        elif pessoa=='F':
            felix=felix+valor
    elif açao=='A':
        recebe= dados[1].upper()
        paga=dados[2].upper()
        valor = int(dados[3])
        if recebe=='D':
            dalia+=valor
        elif recebe=='E':
            eloi+=valor
        elif recebe=='F':
            felix+=valor

        if paga=='D':
            dalia-=valor
        elif paga=='E':
            eloi-=valor
        elif paga=='F':
            felix-=valor

print(dalia,eloi,felix)
