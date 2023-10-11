def decorator(func):
    return func

# @decorator над данной функцией означает, 
# что мы передаем её в декоратор
@decorator
def decorate_example():
    print('Привет Вселенная!')
    
decorate_example()

# Другое объявление декоратора
# Cоздание переменной и присвоение ей декоратора с передаваемой функцией
decorate_example = decorator(decorate_example)
decorate_example()

# Оба объявления правильные, 
# но объявление с собакой более распространено и удобно