import json
import sys


def task() -> float:
    """
    Читает JSON данные из стандартного ввода, вычисляет сумму произведений
    'score' * 'weight' для каждого словаря и возвращает округленную сумму.
    """
    try:
        # Чтение всех строк из стандартного ввода
        input_str = ''.join(sys.stdin.readlines())

        # Парсинг JSON данных
        data = json.loads(input_str)

        # Проверка, что данные представляют собой список
        if not isinstance(data, list):
            raise ValueError("JSON данные должны быть списком словарей.")

        total = 0.0
        for item in data:
            # Проверка наличия необходимых ключей
            if 'score' in item and 'weight' in item:
                score = item['score']
                weight = item['weight']

                # Проверка типов значений
                if isinstance(score, (int, float)) and isinstance(weight, (int, float)):
                    total += score * weight
                else:
                    raise TypeError("Значения 'score' и 'weight' должны быть числами.")
            else:
                raise KeyError("Каждый словарь должен содержать ключи 'score' и 'weight'.")

        # Округление до 3 знаков
        return round(total, 3)

    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON.")
        return 0.0
    except (KeyError, TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
        return 0.0


# Пример использования:
# Если вы запускаете скрипт из консоли, вы можете передать JSON данные через stdin.
# Например:
# echo '[{"score": 0.5, "weight": 2}, {"score": 1.5, "weight": 3}]' | python script.py

print(task())