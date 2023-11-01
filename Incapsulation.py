class Ball:
    def __init__(self):
        self.name = "Oval" # Публичная переменная — public
        self._radius = 5 # Приватная переменная — private
        self.__color = "red" # Защищенная переменная — protected

    # Публичный метод
    def update_name(self, name):
        self.name = name
        print('name update to: ' + self.name)

    # Приватный метод
    def _update_radius(self, radius):
        self._radius = radius
        print('radius update to: ', self._radius)

    # Защищенный метод
    def __update_color(self, color):
        self.__color = color
        print('color update to: ', self.__color)

    def default_color(self):
        print('default color')
        self.__update_color("red")


ball = Ball()

print(ball.name)
print(ball._radius)
# print(ball.__color)

print()
# Вызов публичного метода:
ball.update_name("Happy Oval")
# Вызов приватного метода:
ball._update_radius(5)
# ball.__update_color()

ball.default_color()
# Вызов защищенного метода:
ball._Ball__update_color("blue")