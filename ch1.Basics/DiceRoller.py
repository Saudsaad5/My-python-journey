import random
# make a dictionarie of tuples to store the dice line by line
diceArt = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

# make a list to store the value of the dice you will get randomly from the next loop
dice = []
total = 0

numOfDice = int(input("Enter how many dice you want: "))
# this loop will generate the values of the dices and store it in a list
for die in range(numOfDice):
    dice.append(random.randint(1, 6))

 # this loop will print the dice
 # 5 is the number of lines to draw a die
 # it will print the first line of each die then the next 
for line in range(5):
    for die in dice:
        print(diceArt.get(die)[line], end="")
    print()

# it will take the numbers from our list and sum it
for die in dice:
    total += die
print(f"total: {total}")