def fibonacci_numbers(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_numbers(n-1) + fibonacci_numbers(n-2))

n = 5 # Число членов последовательности

for i in range(n):
    print(fibonacci_numbers(i))
