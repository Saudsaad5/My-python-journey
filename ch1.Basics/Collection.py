#   collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
#
#                                             IT'S JUST AN ARRAY

fruits = ["apple", "orange", "banana", "mango"]

# you can simply print all elements without a loop
print(fruits)

# a loop to print throuh the "LIST"
for fruit in fruits:
    print(fruit)

# to print the list len    
print(len(fruits))

# a way to check if an element is in your list
print("apple" in fruits)

# to add an element at the end of the list
fruits.append("beash")

# to remove an element 
fruits.remove("apple")

# to insert any element at any index
fruits.insert(3,"apple")

# to sort by alphabet
fruits.sort

# you can clear a list by using list.clear()



