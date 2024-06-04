import time


# Default argus are a values we set as default in our functions
def netPrice(price, discount = 0, tax = 0.15):

    return price * (1 - discount) * (1 - tax)

# notes that you can change the defult values when you call 
print(netPrice(50))
print(netPrice(50, 0.10))
print(netPrice(50, 0.1, 0.10))

print("----- EXAMPLE 2 -----")

# note that we satrt with end because a defult value can't be follwed with a non-defult
def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

print(count(10))