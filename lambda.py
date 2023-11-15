def sum_arg(a, b): # Именованная функция
  return a + b

print(sum_arg(12, 25))

# lambda аргумент1, аргумент2, и т.д. : выражение , использующее аргументы

current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x * 2 , current_list))
print(new_list)

#####

maximum = (lambda a, b: a if a > b else b)
print(maximum(23 , 25))
