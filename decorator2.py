def decorator(func):
    def new_func():
	# декоратор заменяет передаваемую нами функцию 
        # на свою и возвращает её
        print('Казнить нельзя, помиловать!')
    return new_func

@decorator
def decorate_example():
    print('Казнить, нельзя помиловать.')

decorate_example()
