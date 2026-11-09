coordenadas=input().split()
xm=int(coordenadas[0])
ym=int(coordenadas[1])
xa=int(coordenadas[2])
ya=int(coordenadas[3])

cruzamentos=abs(xm-xa)+abs(ym-ya)
print(cruzamentos)