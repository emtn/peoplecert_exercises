number_of_pizzas = int(input("give number of pizzas"))
total_price = 0
pizza_price = 5
for i in range(number_of_pizzas):
    bacon = input("you want bacon?")
    pepper = input("you want pepper?")
    total_price+=pizza_price
    if bacon =='y':
        total_price += 0.20*pizza_price
    if pepper=='y':
        total_price += 0.30*pizza_price

print(f"You ordered {number_of_pizzas} and the price is {total_price}")