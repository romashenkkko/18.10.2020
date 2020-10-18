x=int(input('Nm mediei= '))
if (x>0) and (x<=25):
    print('Va fi in clasa A')
if (x>25) and (x<=50):
    print('Va fi in clasa B')
if (x>50) and (x<=75):
    print('Va fi in clasa C')
if (x>75) and (x<=100):
    print('Va fi in clasa D')
if (x>100) and (x<=125):
    print('Va fi in clasa E')
if (x<=0) or (x>125):  
    print('eroare')