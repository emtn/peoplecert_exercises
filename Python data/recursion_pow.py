def power_of(a,b):
    if b==0:
        return 1
    return  a*power_of(a,b-1)


print(power_of(2,4))