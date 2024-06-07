
# dictionary =  a collection of {key:value} pairs
# ordered and changeable. No duplicates
# it's a 4th type of collections

capitals = {        "USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

# if a key isn'e existing it will print none
print(capitals.get("Japan"))
print("-------------------------")
# we can use it in an if statment
if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
print("-------------------------")

# you can use the .update to add a new key and value or to update a valuee
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})

print(capitals)
print("-------------------------")

# you can use .pop(key) to remove a key from a dictionarie 
capitals.pop("China")
# .popitem will remove the last item in your dictionarie
capitals.popitem()

print(capitals)
print("-------------------------")

# you can use .keys() to get the value of the keys
keys = capitals.keys()
for key in capitals.keys():
    print(key)
print("-------------------------")

# same thing here with .values()
values = capitals.values()
for value in capitals.values():
    print(value)
print("-------------------------")

# .items() will return a 2D list of tuples
items = capitals.items()
# we have 2 counters in this loop
for key, value in capitals.items():
    print(f"{key}: {value}")
print("-------------------------")

# finally .clear to clear the whole dictionarie
capitals.clear()
print("-------------------------")