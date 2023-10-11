class SpaceShip:
    def __init__(self,weight):
        self._weight = weight

    weight = property()

    #геттер
    @weight.getter
    def weight(self):
        return self._weight

    #сеттер
    @weight.setter
    def weight(self, value):
        if value <= 100:
            self._weight = 100
        elif value > 5000:
            self._weight = 5000
        else:
            self._weight = value

space_ship_1 = SpaceShip(2000)
print(f"Вес космического корабля составляет {space_ship_1.weight} тонн.")

space_ship_1.weight = -20
print(f"Вес космического корабля составляет {space_ship_1.weight} тонн.")
