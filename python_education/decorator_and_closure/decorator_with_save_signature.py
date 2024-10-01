from functools import wraps


def debug_decorator(function):  # "обертываем" функцию add новыми свойствами
    @wraps(function)  # декоратор копирует метаданные из функции function во wrapper
    def wrapper(*args):
        print(f"Вызываем функцию {function.__name__} с аргументами {args}")
        result = function(*args)
        print(f"Результат функции {function.__name__}: {result}")
        print(f"Результат перемножения аргументов функции {function.__name__}: {args[0] * args[1]}")
        return result
    return wrapper


@debug_decorator
def add(x, y):
    """Функция сложения двух чисел"""
    return x + y


add(90, 40)

print("Имя функции:", add.__name__)  # без @wraps "Имя функции: wrapper"
print(f"Документация функции {add.__name__}:", add.__doc__)  # без @wraps "Документация функции wrapper: None"


# Вызываем функцию add с аргументами (90, 40)
# Результат функции add: 130
# Результат перемножения аргументов функции add: 3600
# Имя функции: add
# Документация функции add: Функция сложения двух чисел
