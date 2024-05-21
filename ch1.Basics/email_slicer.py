# ask the user for an email
email = input("enter your emil: ")

# create a var to get the index of @ in the email
index = email.index("@")

# split the username and the domain by using indexing
username = email[:index]
# +1 so we print after the @
domain = email[index + 1:]

print(f"your username is {username} and domain is {domain}")