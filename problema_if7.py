a=int(input('1 Nm= '))
b=int(input('2 Nm= '))
c=int(input('3 Nm= '))
if (c>0) and (b>0) and (a>0):
    if (b<c):
        print(c)
    if (c<b):
        print(b)
    if (b==c):
        print(c)
if (a<0) or (b<0) or (c<0):
    print(a+b)