def find_common_participants(group1, group2, delimiter=','):
    # Разделяем строки на списки участников и удаляем возможные пробелы
    set1 = set(participant.strip() for participant in group1.split(delimiter))
    set2 = set(participant.strip() for participant in group2.split(delimiter))

    # Находим пересечение двух множеств
    common_participants = set1 & set2

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)
