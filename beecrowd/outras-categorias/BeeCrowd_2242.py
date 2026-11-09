risada=input()
vogais=[]
for letra in risada:
    if letra in 'aeiou':
        vogais+=letra

reverso=vogais[::-1]
if vogais==reverso:
    print('S')
else:
    print('N')
