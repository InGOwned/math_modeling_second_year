def message(func):
    def wrapper(*args, **kwargs):
        print(f"Начало выполнения функции '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"Конец выполнения функции '{func.__name__}'")
        return result
    return wrapper

@message
def some_function():
    print("Работа функции...")

some_function()
