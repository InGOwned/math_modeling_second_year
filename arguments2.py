def decorator(func):
    def wrapper_function(*args, **kwargs):
        #print(*args, **kwargs)
        func(*args, **kwargs)
        print(*args, **kwargs)
    return wrapper_function


@decorator
def greet(*name):
    print(f"Привет {name}!")

greet("Анастасия", "Миша", "Лена")
