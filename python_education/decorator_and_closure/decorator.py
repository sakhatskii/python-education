def debug_decorator(function):
    def wrapper(*args):
        print(f"Вызываем функцию {function.__name__}")
        result = function(*args)
        print(f"Результат функции {function.__name__}: {result}")
        print(f"Результат перемножения аргументов функции {function.__name__}: {args[0] * args[1]}")
        return result
    return wrapper


@debug_decorator
def add(x, y):
    return x + y


add(90, 40)

# Вызываем функцию add
# Результат функции add: 130
# Результат перемножения аргументов функции add: 3600
