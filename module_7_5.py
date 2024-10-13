import os
import time


def display_file_info(directory):
    """Обходит каталог и отображает информацию о каждом файле."""
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)  # Формируем полный путь к файлу

            # Получаем время последнего изменения и размер файла
            last_modified_time = os.path.getmtime(full_path)
            size = os.path.getsize(full_path)
            parent_directory = os.path.dirname(full_path)  # Получаем родительскую директорию

            # Выводим информацию о файле
            print(f"Файл: {full_path}")
            print(f"Родительская директория: {parent_directory}")
            print(f"Размер: {size} байт")
            print(f"Время последнего изменения: {time.ctime(last_modified_time)}")
            print("-" * 40)


# Пример использования функции
if __name__ == "__main__":
    directory = '.'
    display_file_info(directory)