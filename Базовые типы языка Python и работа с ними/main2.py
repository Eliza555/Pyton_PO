# Параметры
disk_size_mb = 1.44  # Объем дискеты в МБ
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
chars_per_line = 25  # Количество символов в строке
bytes_per_char = 4  # Байт на один символ

# Константы
mb_to_bytes = 1024 * 1024  # Перевод МБ в байты

# Общий объем дискеты в байтах
total_disk_size_bytes = disk_size_mb * mb_to_bytes

# Объем одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Количество книг, помещающихся на дискету
books_fit_on_disk = total_disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", books_fit_on_disk)
