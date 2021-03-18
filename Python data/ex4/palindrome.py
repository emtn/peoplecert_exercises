word=input("give me a word")
palin=''

for i in word[::-1]:
    palin = palin+i

if palin == word:
    print("the word is a palindrome")
else:
    print("the word is not a palindrome")

