try:
    # Некоторый код, генерирующий исключение
    raise Exception("Описание ошибки")
    # raise ExceptionType("Optional message")
except Exception as e:
    print("Произошла ошибка:", str(e))
