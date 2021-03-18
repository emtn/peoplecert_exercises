from time import strftime, gmtime
print( " now its ", strftime("%a ,%d-%b-%Y , %H:%M",gmtime()))

print( " now its ", strftime("%c",gmtime()))
print(gmtime()[0])
print(gmtime(1))