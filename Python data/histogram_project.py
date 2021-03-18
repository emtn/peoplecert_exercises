import random

def randomList(n):
    randList=[]
    for i in range(n):
        randList.append(random.randint(1,10))
    print(randList)
    return randList

def frequency(randList):
    randList_set=set(randList)
    randList_set =list(randList_set)
    randList_freq=[]
    for i in randList_set:
        randList_freq.append(randList.count(i))
    for i in range(len(randList_set)):
        print(f"{randList_set[i]}:{'*'*randList_freq[i]}({randList_freq[i]})") #{randList_set[i]} Value 'randList_set' is unsubscriptable
     
lista=randomList(10)
frequency(lista)

        