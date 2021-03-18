import random
a = random.randint(1,10)
print(a)

for i in range(1,7):
    b = int(input( "guess number, try : "))
    if b>a:
        print("your number is bigger")
    elif b<a:
        print ("your number is smaller")
    else:
        print("correct")
        break

