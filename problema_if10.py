a=int(input('Nm de gaini= '))
b=int(input('Nm de boabe= '))
if (b//(a+1)) and (b%(a+1)==0):
    print('Nm de boabe primit= ', int(b/(a+1), 'egalitate'))
elif b/a:
    print(' Curcanul a primit mai mult cu', b%(a+1), 'boabe')