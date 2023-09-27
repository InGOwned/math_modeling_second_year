class Tomato:
    states = {1: "Зелёный",
              2: "Начал созревать",
              3: "Почти зрелый",
              4: "Зрелый"}
    
    def __init__(self, states=states[1]):
        # self.index = index
        self.state = states
        self.stage = 1
    
    def grow(self, states=states):
        self.state = states[self.stage + 1]
        self.stage += 1
    
    def is_ripe(self):
        if self.state == 'Зрелый':
            print("Томат созрел!!")
            return True
        else:
            print("Томат ещё растёт(")
            return False
    
class TomatoBush:
    def __init__(self, n):
        self.tomatoes = []

        for t in range(n):
            t = Tomato()
            self.tomatoes.append(t)
    
    def grow_all(self):
        for vegetable in self.tomatoes:
            vegetable.grow()
    
    def all_are_ripe(self):
        for vegetable in self.tomatoes:
            if vegetable.state == 'Созрел':
                count_of_ripe += 1
        if count_of_ripe == len(self.tomatoes):
            return True
        return False
    
    def give_away_all(self):
        self.tomatoes = []
    
class Gardener:
    def __init__(self, name, bush):
        self.name = name
        self.plant = bush
    
    def work(self):
        self.plant.grow_all
    
    def harvest(self):
        if self.plant.all_are_ripe:
            self.plant.give_away_all
        else:
            print("Ещё не все томаты созрели")
    
    def knowledge_base(self):
        print("Вы можете окучить свой куст с помощью метода grow_all")
        print('Чтобы собрать урожай используйте метод harvest')

bush = TomatoBush(5)  
Maxim = Gardener('Maxim', bush)
Maxim.knowledge_base()


