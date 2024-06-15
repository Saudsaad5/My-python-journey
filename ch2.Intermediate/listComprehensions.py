# List comprehension = A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

regList = []
for x in range(1,11):
    regList.append(x)
print("----- regular list -----")
print(regList)
print("------------------------")

print("----- List comprehension -----")
print("doubles")
#         expression  value  iterable
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

print("triples")
#         expression  value  iterable
triples = [y * 3 for y in range(1, 11)]
print(triples)

print("squares")
#         expression  value  iterable
squares = [z * z for z in range(1, 11)]
print(squares)

print("----- lower to upper -----")
fruits = ["apple", "orange", "banana", "coconut"]
uppercase_words = [fruit.upper() for fruit in fruits]
print(uppercase_words)

print("----- fruit chars -----")
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]

print("-----positive numbers-----")
positive_numbers = [x for x in numbers if x >= 0]
print(positive_numbers)

print("----- negative numbers -----")
negative_numbers = [x for x in numbers if x < 0]
print(negative_numbers)

print("----- even numbers -----")
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

print("----- odd numbers ------")
odd_numbers = [x for x in numbers if x % 2 == 1]
print(odd_numbers)

print("----- grades -----")
grades = [85, 42, 79, 90, 56, 61, 30]
#                 expression  value  iterable  condition
passing_grades = [grade for grade in grades if grade >= 60]
print(grades)
