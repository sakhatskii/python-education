import json

info = {
  "name": "Mikhail",
  "age": 52,
  "car": True,
  "children": [
    {
      "name": "Alexey",
      "age": 24
    },
    {
      "name": "Daniel",
      "age": 8
    }
  ]
}

print(info, "длинна =", len(info), "тип данных =", type(info))  # длинна = 4 тип данных = <class 'dict'>

# Сериализация (преобразование словаря в JSON)
info_json_str = json.dumps(info)
print(info_json_str, "длинна =", len(info_json_str), "тип данных =", type(info_json_str))  # длинна = 118 тип данных = <class 'str'>

# Десериализация (преобразование JSON обратно в словарь)
reconstructed_dict = json.loads(info_json_str)
print(reconstructed_dict, "длинна =", len(reconstructed_dict), "тип данных =", type(reconstructed_dict))  # длинна = 4 тип данных = <class 'dict'>
