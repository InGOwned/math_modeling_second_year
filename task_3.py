from debugger import debug
import math

@debug
def square_root(x):
    return math.sqrt(x)

result = square_root(25)
print(result)
