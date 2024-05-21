# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is value

sum_odd = 0
sum_even = 0
total = 0

#step 1

cardNumber = input("Enter a cridet card number: ")

#to replace any - or spaces
cardNumber = cardNumber.replace("-" , "")
cardNumber = cardNumber.replace(" " , "")

# to revirse the number
cardNumber = cardNumber[::-1]

#step 2

for x in cardNumber[::2]:
    sum_odd += int(x)

#step 3

for x in cardNumber[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even += (1 + (x % 10))
    else:
        sum_even += x

#step 4

total = sum_odd + sum_even

#step 5

if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
