def custom_write(file_name, strings):
    strings_positions = {}  # Словарь для хранения позиций и строк
    file = open(file_name, 'w', encoding='utf-8')  # Открываем файл для записи

    for index, string in enumerate(strings):
        position = file.tell()  # Получаем текущую позицию в байтах
        file.write(string + '\n')  # Записываем строку в файл
        strings_positions[(index + 1, position)] = string  # Сохраняем в словарь

    file.close()  # Закрываем файл в блоке finally
    return strings_positions

# Пример выполнения программы
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)