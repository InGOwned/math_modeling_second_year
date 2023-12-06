def find_number(a, b):
    if b >= a:
        mid = (b + a) // 2
        print(f"Число меньше {mid}?")
        answer = input().lower()
        if answer == 'да':
            return find_number(a, mid - 1)
        if answer == 'нет':
            return find_number(mid + 1, b)
        print("Некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")
        return find_number(a, b)
    return b

num = int(input('Введите число от 1 до 100: '))
if 1 <= num <= 100:
    print("Число корректно")
    print("Начинаю угадывать Ваше число:")
    guess = find_number(1, 100)
    print(f"Ваше число: {guess}")
else:
    print("Число некорректно. Пожалуйста, введите число от 1 до 100.")
