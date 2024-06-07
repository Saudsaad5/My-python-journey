import random

low = 1
high = 100
options = ("Rock", "Paper", "Scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# print a random number from 1 to 100
RanNumber = random.randint(low, high)
print("----- RANDOM NUMBER FROM 1 - 100 -----")
print(RanNumber)

# print a random option form a tuple
ChoNumber = random.choice(options)
print("----- RANDOM OPTION -----")
print(ChoNumber)

# print a random card from a list. note: random.shuffle will just shuffle the exsisting list not craeting a new one or selecting a single card
random.shuffle(cards)
print("----- RANDO CARD -----")
print(cards)

# here's a: GUESS THE NUMBE GAME
# a var to store the number of guesses and a random number
guesses = 0
answer = random.randint(low, high)

# loop to check if your guess is right
while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1
    if guess < answer:
        print(f"{guess} is too low")
    elif guess > answer:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is the right guess")
        break
#printing how many guesses it took you
print(f"This round took you {guesses} guesses")