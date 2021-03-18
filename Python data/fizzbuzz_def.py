def modulo(x,divisor):
    return x%divisor == 0

for i in range(1,101):
    if modulo(i,3):
        if modulo(i,3) and modulo(i,5):
            print("fizzbuzz")
        else:
            print("buzz")
    elif modulo(i,5):
        print("fizz")
    else:
        print(i)