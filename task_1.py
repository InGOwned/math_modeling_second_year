from math import pi, sqrt

def calculate_area(shape:str, *args):
    shape = shape.lower()
    if shape not in ['круг', "квадрат", "прямоугольник", "треугольник"]:
        raise ValueError('Неверное название фигуры')
    if shape in ['круг', "квадрат"] and len(args) != 1:
        raise TypeError('Неверное количество аргументов')
    if shape == 'прямоугольник' and len(args) != 2:
        raise TypeError('Неверное количество аргументов')
    if shape == 'треугольник' and len(args) != 3:
        raise TypeError('Неверное количество аргументов')
    
    for i in args:
        if i < 0:
            raise ValueError('Нужны положительные числовые аргументы')
    
    if shape == 'круг':
        return 2 * pi * args[0]**2
    if shape == "квадрат":
        return args[0]**2
    if shape == 'прямоугольник':
        return args[0] * args[1]
    p = (args[0] + args[1] + args[2]) / 2
    return sqrt(p * (p - args[0]) * (p - args[1])  * (p - args[2]))

print(calculate_area("треугольник", 7, 8, 14))
print(calculate_area("прямоугольник", 7, 8))
