def factorial(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError('Нужно неотрицательное целое число')
    
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

print(factorial(10))
print(factorial(7))
print(factorial(-10))
