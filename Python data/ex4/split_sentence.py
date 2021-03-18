text  = input("give words with commas\n")

x = text.split(',')
x_num =()
print(x)


for item in x:
    if item.isnumeric():
        x_num=x_num+(item,)

print(x_num)
print(max(x_num))
print(min(x_num))