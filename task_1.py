def add_numbers(number):
    def decorator(func):
        def wrapper(x):
            return func(x + number)
        return wrapper
    return decorator

@add_numbers(5)
def my_function(x):
    return x

print(my_function(-5))
