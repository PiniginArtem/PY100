def is_lucky_number(num: int) -> bool:
    if num < 100000:
        raise ValueError("Число отрицательное или не шестизначное")

    if sum([int(digit) for digit in str(num)[:3]]) == sum([int(digit) for digit in str(num)[3:7]]):
        return True
    return False


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
