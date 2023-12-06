# raise ValueError
try:
    raise KeyError  # Генерация исключения вручную
except KeyError:
    print('Я сгенерировал ошибку!')
