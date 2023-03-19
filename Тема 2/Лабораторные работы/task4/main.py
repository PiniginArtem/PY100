BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100
lines = 50
chars = 25

total_chars = pages * lines * chars
total_bytes = total_chars * BYTES_ONE_CHAR

disk_size_mb = 1.44
disk_size_b = disk_size_mb * 1024 * 1024
number_of_books = int(disk_size_b // total_bytes)

print(number_of_books)
