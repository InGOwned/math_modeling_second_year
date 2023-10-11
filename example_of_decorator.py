import time

def logger(func):
    # def wrapper_function(*args, **kwargs):
    def wrapper_function(list_of_num):
        # result = func(*args, **kwargs)
        timer = time.time()
        result = func(list_of_num)
        with open('log.txt', 'w') as f:
            f.write(str(result))
            f.write('\n')
            t = time.time() - timer
            f.write(str(t))
        return result
    return wrapper_function

@logger
def summator(list_of_num):
    return sum(list_of_num)

summator([1,2,3,4])
