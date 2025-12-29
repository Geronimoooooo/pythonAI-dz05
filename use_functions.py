import os
import os.path
import sys

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

def simple_separator():
    separator = print('**********')
    return separator
    pass


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