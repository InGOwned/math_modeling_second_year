def operation_decorator(operator):
    def decorator(func):
        def wrapper(x, y):
            if operator == '+':
                return func(x, y)
            if operator == '-':
                return x - y
            if operator == '*':
                return x * y
            if operator == '/':
                return x / y
            return "Неверный знак действия"
        return wrapper
    return decorator

@operation_decorator('+')
def two_variables(x, y):
    return x + y

print(two_variables(6, 5))
