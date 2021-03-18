def crypto(a,c):
    alist= []
    b=''
    for char in a:
        alist.append(ord(char)+c)
    for num in alist:
        b = b+chr(num)
    return b

x = input("give a sentence")

print(crypto(x, 3))