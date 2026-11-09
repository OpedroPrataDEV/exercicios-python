aX0,aY0,aX1,aY1=map(int,input().split())
bX0,bY0,bX1,bY1=map(int,input().split())
if aX0>bX1 or aX1<bX0 or aY1<bY0 or aY0>bY1:
    print('0')
else:
    print('1')
