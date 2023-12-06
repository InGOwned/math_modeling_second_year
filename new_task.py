import random


class City:
    specialization = "Специализация города отсутствует"

    def __init__(self, name, population, area, culture, specialization=specialization):
        self.__name = name
        self.__population = population
        self.__area = area
        self.__culture = culture
        self.specialization = specialization

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @property
    def area(self):
        return self.__area

    @property
    def culture(self):
        return self.__culture

    def develop(self):
        print(f"{self.name} развивается.")

    def build(self):
        print(f"В {self.name} построен новый дом")

    def cultural_event(self):
        print(f"{self.name} провёл культурное мероприятие")


class DevelopedCity(City):
    def __init__(self, name, population, area, culture):
        super().__init__(name, population, area, culture, specialization='Развивающийся город')

    def develop(self):
        print(f"{self.name} быстро развивается")


class BuildingCity(City):
    def __init__(self, name, population, area, culture):
        super().__init__(name, population, area, culture, specialization='Активно строящийся город')

    def build(self):
        print(f"В {self.name} построен новый небоскрёб")


class CulturalCity(City):
    def __init__(self, name, population, area, culture):
        super().__init__(name, population, area, culture, specialization='Культурный город')

    def cultural_event(self):
        print(f"{self.name} провёл мероприятие мирового уровня")


class Rand:
    def __init__(self):
        self.__cities = []

    def add_city(self, city):
        self.__cities.append(city)

    def play(self):
        if not self.__cities:
            print("Городов для игры не обнаружено")
            return

        city = random.choice(self.__cities)
        print(f'\nВыбран город {city.name} со пециализацией "{city.specialization}"')
        print(f'Его население: {city.population} человек')
        print(f'Его площадь: {city.area} квадратный метров\n')
        city.develop()
        city.build()
        city.cultural_event()
        print()


game = Game()
game.add_city(DevelopedCity("City1", 100000, 500, "Culture1"))
game.add_city(BuildingCity("City2", 50000, 300, "Culture2"))
game.add_city(CulturalCity("City3", 70000, 400, "Culture3"))
game.play()
