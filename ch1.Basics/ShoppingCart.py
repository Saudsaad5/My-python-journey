# a samll exercise for the Lists

foods = []
prices = []
total = 0
count = 1
# a loop to store the data in the lists
while True :
    food = input("Enter a food to buy (q to quit): ")
    # a break to escape the loop
    if food.lower() == "q":
        break
    else:
        # type casting to store numbers
        price = float(input(f"enter the price for a {food}: $"))
        # adding the items to the lists
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
# a loop to print the items from foods list
for food in foods:
    print(f"{count}: {food}")
    count += 1

print()

print("----------------------------------\n")

print("----- TOTAL PRICE -----")
# a loop to add all the prices from the list and store them in the var total
for price in prices:
    total += price

print(f"Your total price is ${total}")