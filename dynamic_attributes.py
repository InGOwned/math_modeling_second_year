class Ball:
    def __init__(self, mass):
        ''' Инициализатор (конструктор) — это
            специальный метод, который вызывается по
            умолчанию когда вы создаете экземпляр класса.
        '''
        print('Я вызвался')

        self.mass = mass
        self.image = 'hexagone'
        self.x = 0
        self.y = 0
        self.state = True 

    # Методы, реализующие поведение экземпляров
    # self – подразумеваемый экземпляр
    def drop(self):
        if self.state:
            print('Я подбросился')
            self.x = 2
        else:
            print('Я проколот')

    def kick(self):
        if self.state:
            print('Я пнулся')
            self.x += 1
        else:
            print('Я проколот')
    
    def fail(self):
        self.state = False


ball = Ball(0.5)
print(ball.image)
print(ball.mass)
ball.image = 'lines'
print(ball.image)

ball.drop()
ball.kick()
print(ball.x)
ball.fail()
ball.kick()
