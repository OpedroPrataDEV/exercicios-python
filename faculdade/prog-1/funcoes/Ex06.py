lista=[1,1,2]
def tribonacci(n):
    for c in range(n-3):
        lista.append(lista[c]+lista[c+1]+lista[c+2])
    print(lista)


tribonacci(12)

