import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    """
    Читает CSV файл, конвертирует его в JSON формат и записывает в output.json с отступами равными 4.
    """
    try:
        # Чтение CSV файла
        with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
            # Создаем DictReader, который автоматически использует первую строку как заголовки
            reader = csv.DictReader(csv_file)

            # Преобразуем все строки в список словарей
            data = list(reader)

        # Запись данных в JSON файл с отступами равными 4
        with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        print(f"Ошибка: Файл {INPUT_FILENAME} не найден.")
    except csv.Error as e:
        print(f"Ошибка при чтении CSV файла: {e}")
    except json.JSONDecodeError as e:
        print(f"Ошибка при сериализации в JSON: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == '__main__':
    # Выполняем конвертацию
    task()

    # Читаем и печатаем содержимое JSON файла
    try:
        with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
            for line in output_f:
                print(line, end="")
    except FileNotFoundError:
        print(f"Ошибка: Файл {OUTPUT_FILENAME} не найден.")
