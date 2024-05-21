# asking the user for a string
name = input(" enter your name: ")

# casting to int
age = int(input(" enter your age: "))

#ask the user for a phone number
phone = input("enter ur phone number: ")
# add an indexing to print the last 4 number [ start : end : step ]
phoneLast4 = phone[6:]
# if statement with a logical operator
if age < 1 or age >= 100:
    print("Your age is out of range")

    # to close the program
    quit()

# a pro way to print with len() to give us the length and capitalize to make the first letter cap
print(f"hello {name.capitalize()} it's made of {len(name)} letters")
print(f"you are a {age} years old")
print(f"your last 4 digits of ur phone number are{phoneLast4}")
# example for if else statements used .upper to convert the small input to cap
answer =input("Do you want food (Y/N)")
if answer.upper() == "Y":
    print("have some food")
elif answer.upper() == "N":
    print("No food for you")
else:
    print("That's not an answer")