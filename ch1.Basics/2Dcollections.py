# 2D collections are just a list inside a list

# our normal lists
frutes =     ["apple", "banana", "beach", "coconut"]
vegetables = ["carrots", "eggplant", "potatoes"]
meats =      ["fish", "chicken", "turkey"]

# a list that contains all the lists
shoppingList = [frutes, vegetables, meats]

# to access an index you can simply look at the 2D list like this: [row][col]
# in this example we will print "banana"
print(shoppingList[0][1])
print()
# to print all the elements in a good way we use a nsted loop
for collection in shoppingList:
    for item in collection:
        print(item, end=" ")
    print()   
