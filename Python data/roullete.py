
import random

def roul():
    a = random.randint(0,36)
    b = ''
    c = ''
    if a<18:
        c="Small"
    else:
        c="Big"
    if a%2==0:
        b='even'
    else:
        b='odd'
    if (a<=10 or 19<=a<=28) and b=='odd':
        color= 'red'
    elif a==0:
        b='zero'
    else:
        color='black'
    print(a,b,c)

for i in range(10):
    roul()

