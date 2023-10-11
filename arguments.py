def decorator(func):
    def wrapper_function(str):
        func(str)
    return wrapper_function


# Аргумент name передается в wrapper_function декоратора и 
# происходит вызов объекта func, который представляет из себя 
# функцию greet с аргументом name. 
@decorator
def greet(name):
    print(f"Привет {name}!")

print("Кому хотите передать привет?")
greet("Анастасия")
