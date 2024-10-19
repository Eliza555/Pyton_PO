numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим пропущенный элемент и его индекс
missing_index = numbers.index(None)

# Создаем новый список, исключая None для расчета среднего арифметического
valid_numbers = [num for num in numbers if num is not None]

# Расчет среднего арифметического
average = sum(valid_numbers) / len(valid_numbers)

# Замена пропущенного элемента средним арифметическим
numbers[missing_index] = average

print("Измененный список:", numbers)

