a=int(input('Introdu punctele 1 elev:'))
b=int(input('Introdu punctele 2 elev:'))
c=int(input('Introdu punctele 3 elev:'))
if (a>b) and (a>c):
    print('punctajul maxim are elevul cu', a, 'puncte')
if (b>a) and (b>c):
    print('punctajul maxim are elevul cu', b, 'puncte')
if (c>b) and (c>a):
    print('punctajul maxim are elevul cu', c, 'puncte')