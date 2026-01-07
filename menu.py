import random
import sys
import os
import os.path

"""
Функция по меню
"""
def show_menu():
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. вернуться в прошлую директорию')
    print('13. сохранить содержимое рабочей директории в файл')
    print('0. выход')
    return

"""
Функция по викторине
"""
def victorina():

    right_data = {
        'saharovBirthDate': '01.01.1921',
        'gagarinBirthDate': '01.01.1934',
        'korolevBirthDate': '01.01.1907',
        'tsiolkovskiyBirthDate': '01.01.1857',
        'pavlovBirthDate': '02.01.1849',
        'paoloBirthDate': '03.02.1931',
        'leoBirthDate': '04.03.1989',
        'jackBirthDate': '05.04.1954',
        'martinBirthDate': '05.02.1956',
        'petrBirthDate': '07.04.1939'
    }

    while True:

        print('Начинаем викторииину по знаменитным людям!')

        asked_persons = ['Андрей Сахаров', 'Юрий Гагарин', 'Сергей Королев', 'Константин Циолковский', 'Иван Павлов', 'Paolo', 'Leo', 'Jack', 'Martin', 'Petr']
        answers = []
        try:
            for randomPerson in range(5):
                randomPerson = random.sample(asked_persons, 1)
                response = input(f'Когда родился {randomPerson}? ')
                answers.append(response)
        except ValueError:
            print('Верный формат — dd.mm.yyyy. Начните викторину заново.')
            break

        correct_answers = list(right_data.values())
        #Проверяем правильные ответы: сравнимваем список из значений словаря right_data и значения списка answers. Считаем, сколько правильных. Вычитаем их из общего кол-ва ответов. Считаем процент.
        matches = 0
        for answer in answers:
            if answer in correct_answers:
                matches += 1
        if matches == 5:
            print('Все правильно! Вау! 100% правильности! Ошибок нет!')
        else:
            print('Есть ошибки, \n ошибок: ', len(answers) - matches, '\n правильно: ', matches, '\n доля правильных ответов: ', (matches / len(answers)) * 100, '%')

        #спрашиваем хочет ли юзер еще раз пройти
        one_more_test = input('Хотите пройти тест еще раз?\n Yes/No \n')
        if one_more_test != 'Yes':
            continue
        elif one_more_test != 'No':
            break
        else:
            print('Я тебя не понял, поэтому заканчиваю')
            break
        print('Викторина окончена!')
    pass

"""
Функция по банковскому счету
"""
def my_bank_account():
    def init_balance_file(filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as balance:
                balance.write('0')

    def init_history_file(filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as history:
                history.write('История баланса\n')

    def show_balance():
        with open("balance.txt", 'r') as balance:
            balance_to_show = int(balance.read())
            return balance_to_show if balance_to_show else 0

    def top_up():
        count = int(input('Введите сумму пополнения: '))
        with open("balance.txt", 'r') as balance:
            balance_top_up = int(balance.read())
            balance_top_up += count
        with open('balance.txt', 'w') as balance:
            balance.write(str(balance_top_up))
        with open('history.txt', 'a') as history:
            history.write(f'Пополнение на: {str(count)}\n')
        return show_balance()

    def buy_smth():
        buy_amount = int(input('Введите сумму покупки: '))
        with open("balance.txt", 'r') as balance:
            balance_to_check = int(balance.read())
            if buy_amount > balance_to_check:
                bad_result = print('Сумма покупки превышает баланс. Увы, купить не выйдет, пополните баланс.')
                return bad_result
            else:
                name_item = input('Введите название покупки: ')
                balance_to_check -= buy_amount
                with open('balance.txt', 'w') as balance:
                    balance.write(str(balance_to_check))
                with open('history.txt', 'a') as history:
                    history.write(f'Покупка на {str(buy_amount)}, для {name_item}\n')
                return show_balance()

    def account_history():
        with open('history.txt', 'r') as history:
            history_to_show = history.read()
            print(history_to_show)

    init_balance_file('balance.txt')
    init_history_file('history.txt')

    while True:
        print(f'Текущий баланс: {show_balance()}')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        simple_separator()
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = top_up()
            pass
        elif choice == '2':
            balance = buy_smth()
            pass
        elif choice == '3':
            account_history()
            pass
        elif choice == '4':
            sys.exit()
            break
        else:
            print('Неверный пункт меню')
    return

def simple_separator():
    separator = print('**********')
    return separator
    pass


def save_directory_in_file(filename='listdir.txt'):
    files = []
    dirs = []

    for item in os.listdir():
        if os.path.isfile(item):
            files.append(item)
        elif os.path.isdir(item):
            dirs.append(item)

    with open(filename, 'w') as f:
        f.write("files: " + ", ".join(files) + "\n")
        f.write("dirs: " + ", ".join(dirs) + "\n")