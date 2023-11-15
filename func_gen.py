def func_gen(break_key):
    p = 0
    while True:
        yield 2**p

        if p == break_key:
            break

        p += 1


# gen = func_gen(3)
# print(type(gen))

# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in func_gen(10):
    print(i)
