from random import randint


count = 3
def random_number() -> int:
    return "".join([str(randint(0, 9)) for _ in range(count)])

print(random_number())
print(random_number())
print(random_number())
