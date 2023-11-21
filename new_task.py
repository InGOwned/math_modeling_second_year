numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Фильтруем список, используя анонимную функцию
filtered_numbers = list(filter(lambda x: x % 3 == 0, numbers))

print("Новый список:")
# Итератор для печати чисел
for num in filtered_numbers:
    print(num, end=' ')

# Рекурсивная функция для вычисления суммы чисел
def sum_numbers(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + sum_numbers(nums[1:])

# Применяем функцию sum_numbers к списку filtered_numbers
sum_of_numbers = sum_numbers(filtered_numbers)

# Выводим сумму чисел
print(f'\n\nСумма чисел нового списка равна {sum_of_numbers}\n')

# Генератор для создания нового списка с квадратами чисел
squared_numbers = (num ** 2 for num in numbers)

print("Квадраты чисел списка numbers:")
# Выводим квадраты чисел
for num in squared_numbers:
    print(num, end=' ')
print()
