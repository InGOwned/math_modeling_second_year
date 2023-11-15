# генератор списков
a = [x**2 for x in range(10)]

print(type(a))
print(a)

# выражение-генератор
b = (x**2 for x in range(10))

print(type(b))

print(next(b))
print(next(b))
print(next(b))
