a=int(input('1 Nm='))
b=int(input('2 Nm='))
if (a%2==0) and (b%2==0):
    if (a>b):
        print(a)
    if (b>a):
        print(b)
if (a%2!=0) and (b%2==0):
    print(b)
if (a%2==0) and (b%2!=0):
    print(a)