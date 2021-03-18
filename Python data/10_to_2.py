number = int(input("give me your number "))
num=number
duo = ''
while number != 0:
    num = number%2
    number = number//2
    
    
    ######
    duo = duo+str(num)
print(duo[::-1])
