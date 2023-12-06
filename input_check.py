try:
    # Предположим, что пользователь вводит числа с консоли
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    
    # Проверяем, что введено неотрицательное число
    if x < 0 or y < 0:
        raise ValueError("Числа должны быть неотрицательными")
    
    result = x / y
    
    print("Результат:", result)

except ValueError as e:
    print("Ошибка:", e)

except ZeroDivisionError:
    print("Ошибка: деление на ноль")

except Exception as e:
    print("Произошла непредвиденная ошибка:", e)
