import test_division

a =''
b=''
praxi =''
while type(a) !=float or type(b) !=float:
    try:
        a=float(input("give first number"))
        b=float(input("give second number"))
    except ValueError:
        print("you need to give a float")
while praxi !='+' and praxi !='-' and praxi !='*' and praxi !='/':
    praxi = input("give praxi ( +,-,*,/)")

if praxi=='+':
    print(a+b)
elif praxi == '-':
    print(a-b)
elif praxi == '*':
    print(a*b)
elif praxi == '/':
    print(test_division.division(a,b))
