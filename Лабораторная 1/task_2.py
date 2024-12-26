# TODO Найдите количество книг, которое можно разместить на дискете

disk_capacity_mb = 1.44  # Емкость дискеты в Мб
pages_per_book = 100      # Количество страниц в книге
lines_per_page = 50       # Количество строк на странице
chars_per_line = 25       # Количество символов в строке
bytes_per_char = 4        # Количество байт для хранения одного символа

disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 * 1024 байт

book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

number_of_books = round(disk_capacity_bytes // book_size_bytes)  # Целочисленное деление

print("Количество книг, помещающихся на дискету:", number_of_books)