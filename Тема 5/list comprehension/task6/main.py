number = 2342354235235

list_digits = [int(digit_str) for digit_str in str(number)]

print(sum(list_digits))
print(sum([digit for digit in list_digits if digit % 2 == 0]))
print(len(list_digits))
print(min(list_digits))
print(list_digits[0] - list_digits[-1])
