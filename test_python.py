import math
#Тест filter
#Тест №1: фильтрация по числам с плавающей точкой, все числа целые, положительный тест
def first_function(lst):
    asd = list(filter(lambda x: not isinstance(x, float), lst))
    return asd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5, 4.2, 9.8]
assert first_function(numbers) == [1, 2, 3, 4, 5, 6, 7, 8, 9], first_function(numbers)

#Тест №2: фильтрация по числам с плавающей точкой, есть числа с плавающей точкой, отрицательный тест
def first_function(lst):
    asd = list(filter(lambda x: not isinstance(x, float), lst))
    return asd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5, 4.2, 9.8]
assert first_function(numbers) == [3.5, 4.2, 9.8], first_function(numbers)

#Тест №3: фильтрация по числам с целым, положительный тест
def second_function(lst):
    asd = list(filter(lambda x: isinstance(x, float), lst))
    return asd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5, 4.2, 9.8]
assert second_function(numbers) == [3.5, 4.2, 9.8], second_function(numbers)

#Тест №4: фильтрация по числам с целым, отрицательный тест
def second_function(lst):
    asd = list(filter(lambda x: isinstance(x, float), lst))
    return asd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5, 4.2, 9.8]
assert second_function(numbers) == [1, 2, 3, 4, 5, 6, 7, 8, 9], second_function(numbers)

#Тест map
#Тест №5: возведение в степень, положительный тест

def first_map_function(lst):
    squared = list(map(lambda x: x ** 2, lst))
    return squared

numbers = [1, 2, 3, 4]
assert first_map_function(numbers) == [1, 4, 9, 16], first_map_function(numbers)

#Тест №6: возведение в степень, отрицательный тест

def first_map_function(lst):
    squared = list(map(lambda x: x ** 2, lst))
    return squared

numbers = [1, 2, 3, 4]
assert first_map_function(numbers) == [1, 5, 6, 20], first_map_function(numbers)

#Тест sorted
#Тест №6: сортировка списка чисел, положительный тест
def first_sorted_function(lst):
    squared = sorted(lst)
    return squared

numbers = [1, 2, 3, 4, 8, 9, 2, 7, 5]
assert first_sorted_function(numbers) == [1, 2, 2, 3, 4, 5, 7, 8, 9], first_sorted_function(numbers)

#Тест №7: сортировка списка чисел, отрицательный тест
def first_sorted_function(lst):
    squared = sorted(lst)
    return squared

numbers = [1, 2, 3, 4, 8, 9, 2, 7, 5]
assert first_sorted_function(numbers) == [1, 2, 3, 4, 5, 7, 8, 9], first_sorted_function(numbers)

#Тест math
#Тест pi

def math_pi():
    some_pi = math.pi
    return some_pi

assert math_pi() == 3.141592653589793, math_pi()

#Тест pi, отрицательный
def math_pi():
    some_pi = math.pi
    return some_pi

assert math_pi() == '3.141592653589793', math_pi()

#Тест sqrtx, положительный
def math_sqrt(sqrt_number):
    some_sqrt = math.sqrt(sqrt_number)
    return some_sqrt

assert math_sqrt(4) == 2, math_sqrt(4)

#Тест pow, положительный
def math_pow(number, degree):
    some_sqrt = int(math.pow(number, degree))
    return some_sqrt

assert math_pow(4, 2) == 16, math_pow(4, 2)

#Тест pow, отрицательный
def math_pow(number, degree):
    some_pow = int(math.pow(number, degree))
    return some_pow

assert math_pow(2, 5) == 16, math_pow(2, 5)

#Тест hypot, положительный
def math_hypot(x, y):
    some_hypot = math.hypot(x, y)
    return some_hypot

assert math_hypot(4, 3) == 5, math_hypot(4, 3)

#Тест hypot, отрицательный
def math_hypot(x, y):
    some_hypot = math.hypot(x, y)
    return some_hypot

assert math_hypot(4, 3) == 9, math_hypot(4, 3)