def division(a,b):
    if b==0:
        print("cannot divide with 0 try again")
        b= int(input("give divisor again"))
        return division(a,b)
    else:
        return a/b
