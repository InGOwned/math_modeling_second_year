"""
Есть пицца, пиццерия, покупатель и доставщик.
Покупатель делает заказ из определённого ресторана, выбирая пиццы из меню.
После этого заказ улетает рандомному доставщику и он его доставляет.
При этом выводится список пицц, которые были заказаны.
Доставщик некоторое время доставляет заказ, после чего выводится сообщение о том,
что заказ успешно доставлен и выводится сумма к оплате.
Пользователь оплачивает заказ и получает сдачу(опционально).
После этого пользователь оценивает полученный заказ.
Успех!
"""

import time
import random

dodo_menu = ["Маргарита", "Пепперони", "Гавайская", "Мексиканская",
             "Вегетарианская", "Сырная", "Мясная", "Четыре сезона",
             "Ранч", "Дьябло"]

papasha_menu = ["Маргарита", "Гавайская", "Мексиканская",
                "Вегетарианская", "Сырная", "Мясная", "Четыре сезона",
                "Ранч", "Дьябло", "Студенто", "Салями"]

tobasco_menu = ["Маргарита", "Пепперони", "Гавайская", "Мексиканская",
                "Вегетарианская", "Сырная", "Ранч", "Дьябло", "Тоскана",
                "Студенто", "Салями"]

price_of_pizzas = {"Маргарита": 350, "Пепперони": 480, "Гавайская": 475, "Мексиканская": 500,
                   "Вегетарианская": 380, "Сырная": 400, "Мясная": 640, "Четыре сезона": 490,
                   "Ранч": 500, "Дьябло": 550, "Тоскана": 550, "Студенто": 470,
                   "Салями": 470}


class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class PizzaRestaurant:
    def __init__(self, name, menu):
        self.order = []
        self.name = name
        self.menu = {i + 1: pizza for i, pizza in enumerate(menu)}

    def get_name(self):
        return self.name

    def get_order(self):
        return self.order

    def show_menu(self):
        print(f"\nДобро пожаловать в ресторан {self.name}!")
        print("Вот наше меню:", end=' ')
        for number, pizza in self.menu.items():
            print(f"{number}. {pizza}", end=' ')
        print()
        print("Что бы вы хотели заказать?")

    def add_pizza(self, pizza):
        self.order.append(pizza)


class PizzaDeliever:
    def __init__(self, name):
        self.name = name
        self.address_to_go = 'Адрес доставки не задан'

    def set_address_to_go(self, address):
        self.address_to_go = address

    def get_name(self):
        return self.name

    def get_address_to_go(self):
        return self.address_to_go

    def delievery(self, restaraunt):
        pizzas_to_deliever = restaraunt.order
        if self.address_to_go == 'Адрес доставки не задан':
            time.sleep(1)
            print()
            print(f'У доставщика {self.name} адрес доставки не задан')
            return False
        if not pizzas_to_deliever:
            time.sleep(2)
            print()
            print(f"Нечего доставлять из ресторана {restaraunt.get_name()}")
            return False

        print()
        print(f'Забирание {len(pizzas_to_deliever)} пицц из ресторана {restaraunt.get_name()} доставщиком'
              f' {self.name}. Список пицц:')
        for pizza in pizzas_to_deliever:
            time.sleep(1)
            print(f'─ {pizza.get_name()}')
            time.sleep(1)

        time.sleep(1)
        print(f'Доставка пицц по адресу {self.address_to_go}')
        time.sleep(2)

        print('Доставка в пути...')
        time.sleep(2)
        print('Доставка в пути...')
        time.sleep(2)

        print('Доставка прибыла!')
        time.sleep(2)

        total_price = sum([pizza.get_price() for pizza in pizzas_to_deliever])

        print(f"К оплате {total_price} рублей")
        time.sleep(1)

        payment = input("Введите сумму для оплаты: ")
        while not payment.strip() or not payment.isdigit():
            if not payment.strip():
                payment = input("Введите сумму для оплаты: ")
            else:
                print("Только число!")
                payment = input("Введите сумму для оплаты: ")

        payment_count = int(payment)
        max_payment = 10000

        while payment_count > max_payment:
            print("Превышен максимальный размер оплаты")
            payment = input("Введите сумму для оплаты: ")
            while not payment.strip() or not payment.isdigit():
                if not payment.strip():
                    payment = input("Введите сумму для оплаты: ")
                else:
                    print("Только число!")
                    payment = input("Введите сумму для оплаты: ")
            payment_count = int(payment)

        while True:
            if payment_count > total_price:
                print(f'Успех! Сдача {payment_count - total_price} рублей. Приятного аппетита!')
                print()
                time.sleep(2)
                break
            if payment_count == total_price:
                print("Успешная оплата! Приятного аппетита!")
                print()
                time.sleep(1)
                break
            if payment_count < total_price:
                print(f"Не хватает ещё {total_price - payment_count} рублей. Доплатите ещё")
            payment = input("Доплата: ")
            while not payment.strip() or not payment.isdigit():
                if not payment.strip():
                    payment = input("Доплата: ")
                else:
                    print("Только число!")
                    payment = input("Доплата: ")
            payment_count += int(payment)

        restaraunt.order = []
        self.address_to_go = 'Адрес доставки не задан'


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_addres(self):
        return self.address

    def make_an_order(self, restaraunt, deliever):
        time.sleep(1)
        restaraunt.show_menu()
        print()

        choice = input("Введите номера или названия пицц через запятую: ")

        while True:
            choices = choice.split(", ")
            # print(f'Отладка: choices: {choices}')
            for c in choices:
                # print(f'{c} попало в цикл for')
                if c.isdigit():
                    # print(f"Число: {c}")
                    number = int(c)
                    if number in restaraunt.menu:
                        pizza = Pizza(restaraunt.menu[number], price_of_pizzas[restaraunt.menu[number]])
                        restaraunt.add_pizza(pizza)
                    # elif c.strip():
                    #     break
                    else:
                        print("Пиццы должны быть из меню ресторана. Попробуйте еще раз.\n")
                        restaraunt.order = []
                        break
                else:
                    c = c.capitalize()
                    # print(f"Строка: {c}")
                    if c in restaraunt.menu.values():
                        pizza = Pizza(c, price_of_pizzas[c])
                        restaraunt.add_pizza(pizza)
                    elif not c.strip():
                        break
                    else:
                        print("Пиццы должны быть из меню ресторана. Попробуйте еще раз.\n")
                        restaraunt.order = []
                        break
            if len(choices) == len(restaraunt.order):
                break
            # print(f'Отладка: choices: {choices}')
            choice = input("Введите номера или названия пицц через запятую: ")

        deliever.set_address_to_go(self.address)

        summ_of_prices = 0
        for pizza in restaraunt.get_order():
            summ_of_prices += pizza.get_price()

        time.sleep(1)
        print(f'Отлично! Сумма заказа равна {summ_of_prices}р. Оплата при получении. Согласны ли вы оформить заказ?')
        a = input().capitalize()
        while a not in ["Нет", "Да"]:
            print('Только "Да" или "Нет"')
            a = input().capitalize()

        if a == 'Нет':
            print('\nХорошо, отменяем\n')
            restaraunt.order = []
            return False

        print(f'Оформлен заказ {len(choices)} пицц на адрес {self.address}, на имя {self.name}')
        time.sleep(2)
        print(f'\nВам назначен доставщик {deliever.get_name()}')
        time.sleep(2)

        deliever.delievery(restaraunt)
        
        self.rate_pizza()

    def rate_pizza(self):
        while True:
            rating = input("Пожалуйста, оцените нашу пиццу по шкале от 1 до 5: ")
            if rating.isdigit() and int(rating) in range(1, 6):
                print("Спасибо за вашу оценку! Мы ценим ваше мнение.")
                print()
                time.sleep(1)
                break
            elif not rating.strip():
                continue
            else:
                print("Пожалуйста, введите число от 1 до 5.")


restaraunt1 = PizzaRestaurant('Додо Пицца', dodo_menu)
restaraunt2 = PizzaRestaurant('Папаша Беппе', papasha_menu)
restaraunt3 = PizzaRestaurant('Тобаско', tobasco_menu)

list_of_restaraunts = {"Додо Пицца": restaraunt1,
                       'Папаша Беппе': restaraunt2,
                       'Тобаско': restaraunt3}

deliever1 = PizzaDeliever('Иван Петрович')
deliever2 = PizzaDeliever('Мухаммед Попович')
deliever3 = PizzaDeliever('Себастьян Никитич')
deliever4 = PizzaDeliever('Валентин Дядька')
deliever5 = PizzaDeliever('Константин Олегович')

list_of_delievers = [deliever1, deliever2, deliever3, deliever4, deliever5]

# customer1 = Customer('Мишаня', 'улица Чкалова, д. 35')
# customer2 = Customer('Алёша', 'улица Рубинштейна, д. 44')
# customer3 = Customer('Максон', 'улица Проспект Мира, д. 62')

while True:
    print('Добро пожаловать в программу заказа пиццы! '
          "Здесь вы можете выбрать пиццы из меню ресторанов, "
          "оформить заказ на доставку и оплатить его.")

    name = input('Представьтесь: ')
    while not name.strip() or name.isdigit():
        if name.isdigit():
            print("Требуется ваше имя")
        name = input("Представьтесь: ")

    address = input('Введите свой адрес: ')
    while not address.strip() or address.isdigit():
        if address.isdigit():
            print("Адрес не может содеражать только числа")
        address = input('Введите свой адрес: ')

    customer = Customer(name, address)
    print("\nСупер!\n")
    print("Список ресторанов, из которых можно сделать заказ:", ", ".join(list_of_restaraunts))
    print()

    choice_of_restaraunt = input('Введите название ресторана, из которого хотите сделать заказ: ')
    while choice_of_restaraunt not in list_of_restaraunts:
        print("Такого ресторана нет в списке")
        print()
        choice_of_restaraunt = input('Введите название ресторана, из которого хотите сделать заказ: ')

    customer.make_an_order(list_of_restaraunts[choice_of_restaraunt],
                           random.choice(list_of_delievers))
    
    


# deliever1.delievery(restaraunt1)
# deliever2.delievery(restaraunt1)
# deliever3.delievery(restaraunt1)
