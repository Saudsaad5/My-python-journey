import random
import string

# we will add all the chars we need to this var using the string method
chars = string.punctuation + string.digits + string.ascii_letters + " "

# now we will type cast it to a list
chars = list(chars)
# will make another copy of the chars LIST!!
key = chars.copy()
# shuffle the list
random.shuffle(key)


#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
# will get each litter index in the chars list
for litter in plain_text:
    index = chars.index(litter)
    # now we add a char from the key list that has the same index as the chars list
    cipher_text += key[index]
print("--------------------------------")
print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")
print("--------------------------------")

#DECRYPT
# The same process but start with the key list
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print("--------------------------------")
print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")
print("--------------------------------")


