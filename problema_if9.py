xa=int(input('Bile mici de culoare alba sunt '))
xr=int(input('Bile mici de culoare rosie sunt '))
xv=int(input('Bile mici de culoare verzi sunt '))
ya=int(input('Bile mari de culoare alba sunt '))
yr=int(input('Bile mari de culoare rosii sunt '))
yv=int(input('Bile mari de culoare verzi sunt '))
ty=yr+ya+yv
tx=xr+xa+xv
if (tx>ty):
    print(tx, 'mici sunt mai multe decat cele mari')
if (ty>tx):
    print(ty, 'mari sunt mai multe decat cele mici')
if (ty==tx):
    print( 'numar egal de bile de ambele marimi')
if ((xa+ya)>(xr+yr)) and ((xa+ya)>(xv+yv)):
    print(xa+ya, ' albe sunt mai multe')
if ((xa+ya)<(xr+yr)) and ((xr+yr)>(xv+yv)):
    print(xr+yr, ' rosii sunt mai multe')
if ((xa+ya)<(xv+yv)) and ((xr+yr)<(xv+yv)):
    print(xv+yv, ' verzi sunt mai multe')
if ((xa+ya)==(xr+yr)) and ((xa+ya)>(xv+yv)):
    print(xa+ya, ' numar de albe care este egal cu numarul de rosii')
if ((xa+ya)>(xr+yr)) and ((xa+ya)==(xv+yv)):
    print(xa+ya, ' numar de albe care este egal cu numarul de verzi')
if ((xa+ya)<(xv+yv)) and ((xr+yr)==(xv+yv)):
    print(xr+yr, 'numarul de rosii care e egal cu numarul de verzi')
