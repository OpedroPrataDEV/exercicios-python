band=int(input())
quedas=0
for c in range(band):
    latas,copos=map(int,input().split())
    if latas>copos:
        quedas+=copos
print(quedas)