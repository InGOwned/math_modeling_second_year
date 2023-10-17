import functools

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [str(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем функцию {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула значение {value}")
        return value

    return wrapper_debug
