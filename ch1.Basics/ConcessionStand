# Concession stand program

# we will create a dictionarie to store our menu
menu = {       "pizza": 3.00,
               "nachos": 4.50,
               "popcorn": 6.00,
               "fries": 2.50,
               "chips": 1.00,
               "pretzel": 3.50,
               "soda": 3.00,
               "lemonade": 4.25}

# a list to store the selected items and an int var to store the total
cart = []
total = 0

# a loop to print the menu by using .items
print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

# this loop will ask the user to slelct an item from the menu and store it in the cart
while True:
    food = input("Select an item (q to quit)").lower()
    # break condtion
    if food == "q":
        break
    # it informs the user if the item isn't in the menu
    elif menu.get(food) is None:
        print(f"{food} isn't in the menu")
    # to store the selected item in the card
    elif menu.get(food) is not None:
        cart.append(food)

# this loop will print the selected items from the card and calc the total
print("------ YOUR ORDER ------")
for item in cart:
    print(item, end=" ")
    total += menu.get(item)
print()
# print the total
print(f"Your total is: {total:.2f}")