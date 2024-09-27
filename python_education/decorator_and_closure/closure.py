def outer_function(x):  # внешняя функция, создающая замыкание
    def inner_function(y):  # внутренняя функция, использующая значение x
        return x * y
    return inner_function

closure = outer_function(7)  # cоздаем замыкание с x == 7

print(closure(5))  # 35 (7 * 5)
