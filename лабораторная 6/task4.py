import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as fn:
        table = []
        for index, line in enumerate(fn):
            # Получаем поля из строки
            fields = line.strip(new_line).split(delimiter)
            # Если мы на первой строке, сохраняем поля как заголовки
            if index == 0:
                heads = fields
                continue

            # Добавляем новый словарь в таблицу
            table.append({})

            for i, _ in enumerate(heads):
                # Берем последний элемент таблицы (добавленный словарь)
                # Добавляем в него нужный элемент
                table[-1][heads[i]] = fields[i]
    return table

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


