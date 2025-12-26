import os

import menu

#Тест №1: тестирование разделителя с import

assert menu.simple_separator() == '**********'

#Тест №2: тестирование функции пополнения, импортировать ее нецелесообразно из-за input в коде

balance = 0
history = []
def top_up(balance, history):
    count = 1000
    balance += count
    history.append(f'Пополнение на: {count}')
    return balance

assert top_up(balance, history) == 1000

#Тест №2: тестирование функции пополнения, негативный тест

balance = 0
history = []
def top_up(balance, history):
    count = 1000
    balance += count
    history.append(f'Пополнение на: {count}')
    return balance

assert top_up(balance, history) == 2000

i = 0
def some_mkdir(i):
    if not os.path.exist(f'new{i}'):
        os.mkdir(f'new{i}')
        i += 1
    assert f'new{i}' in os.listdir()