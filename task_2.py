from random import randint


class Pyramyd:
    def __init__(self, max_h):
        self.max_bricks_count = 0
        self.bricks_count = 0
        self.current_h = 0
        self.current_row = 0

        if max_h <= 0:
            self.max_h = 10
            self.max_len_current_row = 10
            for i in range(10, 0, -1):
                self.max_bricks_count += i
        else:
            self.max_h = max_h
            self.max_len_current_row = max_h
            for i in range(max_h, 0, -1):
                self.max_bricks_count += i
        
        
    def add_bricks(self, n):
        self.bricks_count += n

    def get_height(self):
        return self.current_h

    def is_done(self):
        return int(self.current_h * 100 / self.max_h)


class Builder:
    def __init__(self, n, h):
        if 0 < n or n > 15:
            self.bricks = 15
        else:
            self.bricks = n
        self.my_pyramyd = Pyramyd(h)
        self.day_counter = 1

    def buy_bricks(self, n):
        self.bricks += n

    def build_pyramyd(self, n):
        if n > self.bricks:
            print("Не хватает", n - self.bricks, "кирпичей. Приобретите ещё")
            return 1
        else:
            if self.my_pyramyd.current_row < self.my_pyramyd.max_len_current_row:
                self.my_pyramyd.current_row += n
                self.bricks -= n
                self.my_pyramyd.add_bricks(n)
                print("Положено", n, "кирпичей")
            else:
                if self.my_pyramyd.bricks_count > self.my_pyramyd.max_bricks_count:
                    return 2
                else:
                    # print(f"Moving to the next level: current_max_len={self.my_pyramyd.max_len_current_row}, current_row={self.my_pyramyd.current_row}")
                    
                    print("Вчера была достигнута максимальная длина ряда")

                    self.my_pyramyd.current_h += 1


                    if self.my_pyramyd.current_row - self.my_pyramyd.max_len_current_row != 0 and self.my_pyramyd.current_h != self.my_pyramyd.max_h:
                        print(f"Перенос {self.my_pyramyd.current_row - self.my_pyramyd.max_len_current_row} кирпичей на следующий ряд")
                    print("Начало строительства следующего ряда")    
                    
                    self.my_pyramyd.current_row -= self.my_pyramyd.max_len_current_row
                    self.my_pyramyd.max_len_current_row -= 1
                    # elif self.my_pyramyd.current_h != self.my_pyramyd.max_h:
                        
            
            # print(f'Bricks_count = {self.my_pyramyd.bricks_count}, max_bricks_count = {self.my_pyramyd.max_bricks_count}')

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
                # print()
                print("Ваш строитель положил слишком много кирпичей. Пирамида разрушена")
                return False
            else:
                print("Осталось", self.bricks, "кирпичей у строителя")
                print("Высота пирамиды:", self.my_pyramyd.get_height(), "кирпичей")
                print("Готовность пирамиды:", self.my_pyramyd.is_done(), "%")
                self.day_counter += 1
                
        print()
        print("Пирамида готова!")
        print()

a = int(input("Введите начальное кол-во кирпичей у строителя, от 0 до 15: "))
b = int(input("Введите высоту пирамиды: "))

builder = Builder(a, b)

while True:
    builder.work_day()
    break

if a < 0 or a > 15:
    print()
    print("Не более 15 и не менее 0))) Приравниваем количество кирпичей у строителя к 15")
if b <= 0:
    print()
    print("Высота не может равняться нулю или быть меньше нуля. Приравнивается к десяти")
