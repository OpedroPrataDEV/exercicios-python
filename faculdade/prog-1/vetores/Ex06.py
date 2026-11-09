candidatos=int(input('Número de candidatos: '))
lista_nomes=[]
lista_media=[]
for c in range(candidatos):
    soma = 0
    lista_nomes.append(input('Nome do candidato: '))
    nota1=int(input('Nota 1: '))
    soma+=nota1
    nota2=int(input('Nota 2: '))
    soma+=nota2
    nota3=int(input('Nota 3: '))
    soma+=nota3
    media=soma/3
    lista_media.append(media)
for vaga in range(candidatos):
    for j in range(0, candidatos - vaga - 1):
        if lista_media[j] > lista_media[j + 1]:
            aux_media = lista_media[j]
            lista_media[j] = lista_media[j + 1]
            lista_media[j + 1] = aux_media
            aux_nome = lista_nomes[j]
            lista_nomes[j] = lista_nomes[j + 1]
            lista_nomes[j + 1] = aux_nome
for i in range(candidatos):
    print(f"{i + 1}º Lugar: {lista_nomes[i]} - Média: {lista_media[i]:.2f}")





