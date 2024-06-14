# validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# ask the user for an input
usernamr = input("enter a username: ")

# to see if the input is less than 12 char
if len(usernamr) > 12:
    print("your username is too long")
# .find return a boolean so if it's not -1 then means it found a space
elif not usernamr.find(" ") == -1:
    print("your name can't have spaces")
# .isalpha checks if it's all letters so if it's not it means there's a number
elif not usernamr.isalpha():
    print("your username can't have numbers")
else:
    print(f"Welcome {usernamr}")
