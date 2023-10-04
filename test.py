list_of_pizzas = ["Маргарита", "Пепперони", "Гавайская", "Мексиканская",
                  "Вегетарианская", "Сырная", "Мясная", "Четыре сезона",
                  "Мексиканская", "Ранч"]


class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name


class PizzaRestaurant:
    def __init__(self, name):
        self.order = []
        self.name = name
    
    def get_name(self):
        return self.name
    
    def add_pizza(self, pizza):
        self.order.append(pizza)
    
    def get_order(self):
        return self.order


class PizzaDeliever:
    def __init__(self, name):
        self.name = name
        self.address_to_go = ''

    # def set_address_to_go(self, address=str):
    #     self.address_to_go = address

    def get_address(self):
        return self.address_to_go
    
    def delievery(self, restaraunt=PizzaRestaurant, address=str):
        pizzas_to_deliever = restaraunt.order

        print(f'Забирание {len(pizzas_to_deliever)} пицц из ресторана {restaraunt} доставщиком {self.name}. Список пицц:')
        
        for pizza in pizzas_to_deliever:
            print(f'─ {pizza}')
        
        print(f'Доставка пицц по адресу {address}')
        print('Доставка успешна!')

        restaraunt.order = []


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_name(self):
        return self.name
    
    def make_an_order(self, pizzas, restaraunt=PizzaRestaurant, deliever=PizzaDeliever):
        deliever.set_address(self.address)
        restaraunt.add_pizza(pizzas)






restaraunt1 = PizzaRestaurant('ДодоПицца')
deliever1 = PizzaDeliever('Иван Петрович')
customer1 = Customer('Мишаня', 'улица Чкалова, д. 35')
    
