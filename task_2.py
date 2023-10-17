def operation_decorator(func):
    def wrapper(x, y, operator):
        if operator == '+':
            return func(x, y) + func(y, x)
        elif operator == '-':
            return func(x, y) - func(y, x)
        elif operator == '*':
            return func(x, y) * func(y, x)
        elif operator == '/':
            return func(x, y) / func(y, x)
        else:
            return "Неверный знак действия"
    return wrapper

@operation_decorator
def two_variables(x, y):
    return x

print(two_variables(6, 5, '+'))
