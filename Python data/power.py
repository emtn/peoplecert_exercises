def power(x,n):
    if n == 0:
        return 1
    if n>=0:
        return power(x,n-1)*x
    else:
        return power(x,n+1)*1/x

print(power(2,-3))