a=int(input('1 Nota:'))
b=int(input('2 Nota:'))
c=int(input('3 Nota:'))
if (c>8):
    print(a, b, c)
if (c<8):
    if (a>b):
        print(a)
    if (b>a):
        print(b)