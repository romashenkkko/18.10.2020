a=int(input('1 Nm='))
b=int(input('2 Nm='))
c=int(input('3 Nm='))
if (a%2==0) and (b%2==0) and (c%2==0):
    print(a, 'PAR')
    print(b, 'PAR')
    print(c, 'PAR')
elif (a%2==1) and (b%2==0) and (c%2==0):
    print(a, 'IMPAR')
    print(b, 'PAR')
    print(c, 'PAR')
elif (a%2==0) and (b%2==1) and (c%2==0):
    print(a, 'PAR')
    print(b, 'IMPAR')
    print(c, 'PAR')
elif (a%2==0) and (b%2==0) and (c%2==1):
    print(a, 'PAR')
    print(b, 'PAR')
    print(c, 'IMPAR')
elif (a%2==0) and (b%2==1) and (c%2==1):
    print(a, 'PAR')
    print(b, 'IMPAR')
    print(c, 'IMPAR')
elif (a%2==1) and (b%2==1) and (c%2==0):
    print(a, 'IMPAR')
    print(b, 'IMPAR')
    print(c, 'PAR')
elif (a%2==1) and (b%2==0) and (c%2==1):
    print(a, 'IMPAR')
    print(b, 'PAR')
    print(c, 'IMPAR')
else:
    print(a, 'IMPAR')
    print(b, 'IMPAR')
    print(c, 'IMPAR')