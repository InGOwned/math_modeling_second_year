class CustomException(Exception):
    pass

def event_handler():
    # Здесь происходит обработка события
    event_occurred = True
    
    if event_occurred:
        raise CustomException("Событие произошло")

try:
    event_handler()
except CustomException as e:
    print(e)   