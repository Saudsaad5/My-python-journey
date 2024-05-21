

name = input("enter your name: ")

while name == "":
    print(" you did'nt enter your name")
    name = input("enter your name: ")
print(f"Hello {name}")

age = int(input("enter your age: "))

while age < 0 :
    print("Age can't be nigative")
    age = int(input("enter your age: "))
print(f"You are {age} years old")

food = input("Enter a food u like (q to quit)")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter a food u like (q to quit)")
print("bye bye.")

num = int(input("enter a number between 1 - 10"))

while num < 1 or num > 10 :
    print(f"{num} is not valid")
    num = int(input("enter a number between 1 - 10"))
print(f"your nubmer is{num}")