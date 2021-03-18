def row(i):
    s1 = '|'*i+' '
    s2 = '   '
    print(f"{' ---'*i}")

    print(s2.join(s1)+"\b|")

    print(f"{' ---'*i}")
size=int(input("give board size"))
for i in range(size):
    row(size)