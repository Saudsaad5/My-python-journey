# *args = allows you to pass multiple non-key argus
# **kwargs = allows you to pass multiple keyword argus


# ----- *ARGS Example 1 -----
# *args will be stored as a tuple

def add(*nums):
   total = 0
   for num in nums:
       total += num
   return total

print(add(1, 2, 3, 4))
print("---------------------------")

# ----- *ARGS Example 2 -----

def display_name(*args):
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
print()

# ----- **KWARGS -----
# **kwargs will be stored as a dictionarie
def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")

print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="Detroit",
              state="MI",
              zip="54321")
print()

# ----- EXERCISE FOR BOTH -----
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               apt=" #1001",
               city="Detroit",
               state="MI",
               zip="54321")

