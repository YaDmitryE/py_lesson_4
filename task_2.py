# Введите пятизначное целое число
number = int(input("Введите пятизначное целое число: "))

# Разделяем число на его составляющие
units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

# Вычисляем результат по заданной формуле
result = (tens ** units) * (hundreds * 1) / (ten_thousands - thousands)

# Выводим результат
print(result)
