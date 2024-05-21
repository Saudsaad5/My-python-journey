# print only the last for digits of this card number: 1234-5678-9012-3456
# print it in reverse too
# remember that indexing form is [ start : end : step ]

cridet_number = "1234-5678-9012-3456"

# started from the end -1 -2 -3 -4
last_digits = cridet_number[-4:]
revers_num = cridet_number[::-1]

print(f"XXXX-XXXX-XXXX-{last_digits}")
print(revers_num)