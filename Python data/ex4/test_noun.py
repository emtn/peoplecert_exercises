import random
def histogram(num,times):
    print("{} :{}({})".format(num,"*"*times,times))

def randomList(num):
    li = []
    for i in range(1,num+1):
        li.append(random.randint(1,6))
    return li

def frequency(li):
    num_li = []
    count_li =[]
    for num in li:
        if num not in num_li:
            num_li.append(num)
    for num in num_li:
        count_li.append(li.count(num))
    return (num_li,count_li)

num = int(input("Give the length of list"))
li = randomList(num)
print(li)
num_li = frequency(li)[0]
count_li = frequency(li)[1]
for i in range(len(num_li)):
histogram(num_li[i],count_li[i])        