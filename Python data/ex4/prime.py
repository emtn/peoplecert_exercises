def check(x):
    flag = ''
    for i in range(2,x):
        if x % i == 0:
            flag = 'not_prime'
            break
        else:
            flag='prime'
    if flag == 'prime': prime_list.append(x)
prime_list = [2]
for a in range(1,100):
    check(a)
print(prime_list)