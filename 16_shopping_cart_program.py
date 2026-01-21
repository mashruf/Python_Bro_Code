foods = []
prices = []
total = 0


while True:
    food = input("Enter food you want to buy('q' to quit): ")
    
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input("Enter price of the food: "))
        prices.append(price)

print("-----Your Cart-----")

for x in foods:
    print(x, end=" ")
print()

for y in prices:
    total = total + y


print(f'Your total bill is {total} taka')