class Human:
    default_name = 'Ivan'
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 2000000
        self._house = "Сейчас дома нет"
    
    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f"Кол-во денег: {self._money}")
        print(self._house)

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)
    
    def _make_deal(self, house):
        self._money -= house._price
        self._house = house
    
    def earn_money(self, amount):
        self._money += amount
    
    def buy_house(self, house):
        if house._price > self._money:
            print("Денег на дом нема")
        else:
            print("Денег хватает, дом приобритён!")
            self._make_deal(house)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, discount):
        self._price -= (discount / 100) * self._price


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


Human.default_info()

human = Human('Misha', 27)
human.info()

house = SmallHouse(4000000)
human.buy_house(house)


