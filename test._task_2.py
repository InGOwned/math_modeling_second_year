from random import randint


class Pyramyd:
    def __init__(self, max_h):
        self.max_h = max_h
        self.x = max_h
        self.bricks_count = 0
        self.current_h = 0
        self.current_row = 0

    def add_bricks(self, n):
        self.bricks_count += n

    def get_height(self):
        return self.current_h

    def is_done(self):
        return int(self.current_h * 100 / self.max_h)


class Builder:
    def __init__(self, n):
        self.bricks = n
        self.my_pyramyd = Pyramyd(11)
        self.day_counter = 1

    def buy_bricks(self, n):
        self.bricks += n

    def build_pyramyd(self, n):
        if n > self.bricks:
            print("Не хватает", n - self.bricks, "кирпичей. Приобретите ещё")
            return 1
        else:
            self.bricks -= n
            # self.my_pyramyd.add_bricks(n)
            if self.my_pyramyd.current_row <= self.my_pyramyd.x:
                self.my_pyramyd.current_row += n
            else:
                if self.my_pyramyd.current_row - self.my_pyramyd.x > self.my_pyramyd.x - 1 and self.my_pyramyd.current_row != 2:
                    return 2
                else:
                    self.my_pyramyd.current_row -= self.my_pyramyd.x
                    self.my_pyramyd.x -= 1
                    self.my_pyramyd.current_h += 1

    def work_day(self):
        while self.my_pyramyd.is_done() != 100:
            a = randint(1, 5)
            print()
            print("День", self.day_counter)
            result = self.build_pyramyd(a)
            if result == 1:
                print("Покупка", 15 - self.bricks, "кирпичей")
                self.buy_bricks(15 - self.bricks)
                self.day_counter += 1
            elif result == 2:
                print("Пирамида разрушена")
                return False
            else:
                print("Положено", a, "кирпичей")
                print("Осталось", self.bricks, "кирпичей у строителя")
                print("Высота пирамиды:", self.my_pyramyd.get_height(), "кирпичей")
                print("Готовность пирамиды:", self.my_pyramyd.is_done(), "%")
                self.day_counter += 1
                
        print()
        print("Пирамида готова!")
        print()


b = Builder(13)

while True:
    b.work_day()
    break