class Human:
    default_name = 'Ivan'
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 2000000
        self._house = "Сейчас дома нет"
    
    def info(self):
        print('\nСведения о человеке')
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f"Кол-во денег: {self._money} руб.")
        print(self._house, '\n')

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)
    
    def _make_deal(self, house):
        self._money -= house.get_price()
        self._house = f'Имеется {house.condition()} стоимостью {house.get_price()} рублей'
    
    def earn_money(self, amount):
        print(f'Человек получил на счёт {amount} рублей\n')
        self._money += amount
    
    def buy_house(self, house):
        if house.get_price() > self._money:
            print("Попытка купить дом не удалась. Денег на дом нема\n")
        else:
            print("Денег хватает, дом приобритён!")
            self._make_deal(house)


class House:
    def __init__(self, area, price, condition="обычный дом"):
        self._area = area
        self._price = price
        self.__condition = condition
        # self._address = address
    
    def final_price(self, discount):
        self._price -= (discount / 100) * self._price
    
    def get_price(self):
        return self._price
    
    def condition(self):
        return self.__condition

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price, condition='маленький дом')

# Human.default_info()

human = Human('Валера', 27)
# human.info()

house = SmallHouse(4000000)
human.buy_house(house)
human.earn_money(3000000)
human.buy_house(house)

human.info()
