class MyError(Exception):
    pass

def stuff(file):
    raise MyError()

file = open('data.txt', 'w')  

try:
    stuff(file)  # Генерирует исключение
finally:
    file.close()  
    
print('not reached')  # Продолжение при остутствии ошибок
