class Ball:
    color = 'red'
    radius = 5
    weight = 3

    def info():
        print('Great class!')


ball = Ball()

print(ball.color)
# print(ball.info())
print(Ball.radius, Ball.weight)
Ball.info()

ball.color = 'white'

print(ball.color) # white
print(Ball.color) # red

Ball.color = 'white'
new_ball = Ball()

print(new_ball.color)
