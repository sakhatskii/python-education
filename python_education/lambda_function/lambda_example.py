list_number = [1, 2, 3, 4, 5]
dict_name = {"Misha":1990, "Anna":1985, "Dima":1995, "Egor":1980, "Alex":2000}

list_square_number = list(map(lambda x: x**3, list_number))  # возводим все элементы списка в куб
print(list_square_number)  # [1, 8, 27, 64, 125]

list_filter_numbers = list(filter(lambda x: x % 2 == 0, list_number))  # фильтруем список, оставляем четные
print(list_filter_numbers)  # [2, 4]

sorted_dict_name = dict(sorted(dict_name.items(), key=lambda item: item[1]))  # сортируем список по годам
print(sorted_dict_name)  #  {'Egor': 1980, 'Anna': 1985, 'Misha': 1990, 'Dima': 1995, 'Alex': 2000}
