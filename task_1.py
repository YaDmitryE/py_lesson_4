# https://github.com/YaDmitryE/py_lesson_4

# Вводим длину и ширину прямоугольника
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

# Вычисляем площадь и периметр прямоугольника
area = length * width
perimeter = 2 * (length + width)

# Выводим результаты
print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")
