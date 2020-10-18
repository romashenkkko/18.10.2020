
ac=int(input('anul curent = '))
lc=int(input('luna curenta = '))
zc=int(input('ziua curenta = '))
an=int(input('anul nasterii = '))
ln=int(input('luna nasterii = '))
zn=int(input('ziua nasterii = '))
varsta=(ac-an)
if (ac>an):
    if lc<ln :
        print ((varsta-1),' ani')
    elif (lc==ln) and (zc<zn):
        print ((varsta-1),' ani')
    elif (lc==ln) and (zc>=zn):
        print ((varsta),' ani')
    elif lc>ln :
        print (varsta, ' ani')
    else:
        print ('Eroare')