a = range (3) # range допускает множество итераторов
# next(a)

new_a = iter(a)

print(next(new_a))
print(next(new_a))
print(next(new_a))
