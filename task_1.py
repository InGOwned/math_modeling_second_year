def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_squares():
    n = 1
    while True:
        if is_prime(n):
            yield n * n
        n += 1

# Генератор
# gen = prime_squares()

# for _ in range(10):
#     print(next(gen))

gen = prime_squares()

for square in gen:
    print(square)
    if square > 10000:
        break

