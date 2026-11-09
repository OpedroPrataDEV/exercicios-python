port=list(map(int,input().split()))
mat=list(map(int,input().split()))
fis=list(map(int,input().split()))
qui=list(map(int,input().split()))
bio=list(map(int,input().split()))

k=int(input())

port=port[1:]
mat=mat[1:]
fis=fis[1:]
qui=qui[1:]
bio=bio[1:]

valores=[]

for p in port:
    for m in mat:
        for f in fis:
            for q in qui:
                for b in bio:
                    valores.append(p+m+f+q+b)

valores.sort(reverse=True)
print(valores[:k])
