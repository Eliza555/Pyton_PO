# Список игроков
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем общее количество игроков
total_players = len(list_players)
print("Общее количество игроков:", total_players)

# Индекс середины списка
middle_index = total_players // 2

# Формируем команды с помощью слайсирования
first_team = list_players[:middle_index]   # Первая команда
second_team = list_players[middle_index:]   # Вторая команда

# Печатаем команды
print(first_team)
print(second_team)

