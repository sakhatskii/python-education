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

info_json_str = json.dumps(info)  # сериализация (преобразование словаря в JSON)
print(info_json_str, "длинна =", len(info_json_str), "тип данных =", type(info_json_str))  # длинна = 118 тип данных = <class 'str'>

reconstructed_dict = json.loads(info_json_str)  # десериализация (преобразование JSON обратно в словарь)
print(reconstructed_dict, "длинна =", len(reconstructed_dict), "тип данных =", type(reconstructed_dict))  # длинна = 4 тип данных = <class 'dict'>
