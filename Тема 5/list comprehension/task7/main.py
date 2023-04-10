def task(num: int) -> bool:
    if sum([int(digit) for digit in str(num).replace("-", "")]) < 10:
        return False
    return True


print(task(12))
print(task(555))
print(task(-12))
print(task(-149))
