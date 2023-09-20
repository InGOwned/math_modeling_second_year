class Ball:

    # Создаем статические атрибуты класса
    color = 'red'
    radius = 5

ball = Ball()

# Вызов пользовательских атрибутов
print(ball.color)
print(Ball.radius)

# Вызов встроенных атрибутов
print(dir(ball))
# print()
# print(dir(Ball))
# print(ball.__init__())
# print(Ball.__init__)
# print(help(Ball.__init__))

# Изменение пользовательских атрибутов экземпляра
ball.color = 'white'
print(ball.color)
print(Ball.color)

# Изменение пользовательских атрибутов класса
Ball.color = 'white'
new_ball = Ball()
print(Ball.color)
print(new_ball.color)