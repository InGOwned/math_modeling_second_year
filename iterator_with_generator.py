def solar_sys_generate():
    # Создадим итератор при помощи генератора
    for i in ['mercury', 'earth', 'venus']:
        yield i

planets = solar_sys_generate()

print(next(planets))
print(next(planets))
print(next(planets))
