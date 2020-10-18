a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if (a<32000) and (b<32000) and (c<32000):
    if (a>(b+c)) or (b>(a+c)) or (c>(b+a)):
        print('DA')
    else:
        print('NU')