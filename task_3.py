class Tomato:
    states = {0: "Отсутствует",
              1: "Зелёный",
              2: "Начал созревать",
              3: "Почти зрелый",
              4: "Зрелый"}

    def __init__(self, state=1):
        self.state = self.states[state]

    def grow(self):
        if self.state == self.states[0]:
            self.state = self.states[1]
        elif self.state == self.states[1]:
            self.state = self.states[2]
        elif self.state == self.states[2]:
            self.state = self.states[3]
        elif self.state == self.states[3]:
            self.state = self.states[4]

    def is_ripe(self):
        if self.state == self.states[4]:
            return True
        return False


class TomatoBush:
    def __init__(self, n):
        self.tomatoes = []
        for _ in range(n):
            new_tomato = Tomato()
            self.tomatoes.append(new_tomato)

    def grow_all(self):
        for vegetable in self.tomatoes:
            vegetable.grow()

    def all_are_ripe(self):
        count_of_ripe = 0
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                count_of_ripe += 1
        if count_of_ripe == len(self.tomatoes):
            return True
        return False

    def give_away_all(self):
        for tomato in self.tomatoes:
            tomato.state = tomato.states[0]


class Gardener:
    def __init__(self, name, bush):
        self.name = name
        self.bush = bush

    def work(self):
        self.bush.grow_all()
        print('Вы поухаживали за томатами и они стали ближе к созреванию')

    def harvest(self):
        c = 0
        for tomato in self.bush.tomatoes:
            if tomato.state == tomato.states[0]:
                c += 1

        if c == len(self.bush.tomatoes):
            print('Томаты отсутствуют на кусте')
        elif self.bush.all_are_ripe():
            self.bush.give_away_all()
            print("Весь урожай собран!")
        else:
            print("Томаты ещё не созрели")

    def knowledge_base(self):
        print("Вы можете окучить свой куст с помощью метода grow_all")
        print('Чтобы попробовать собрать урожай используйте метод harvest')
        print()


bush1 = TomatoBush(5)
Maxim = Gardener('Maxim', bush1)

Maxim.knowledge_base()

Maxim.work()
Maxim.work()
Maxim.harvest()
Maxim.work()
Maxim.work()
Maxim.harvest()
Maxim.harvest()
Maxim.work()
Maxim.work()
Maxim.work()
Maxim.work()
Maxim.harvest()
