print('recursion:')
def func_factorial(n):
  if 1 == n:
    return n
  return n + func_factorial(n - 1)

print(func_factorial(5))
