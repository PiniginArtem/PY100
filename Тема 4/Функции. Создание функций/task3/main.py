def factorial(n):
    if n < 1:
        return 'Я не могу посчитать'
    n_factorial = 1
    while n >= 1:
        n_factorial *= n
        n -= 1
    return n_factorial

print(factorial(5))