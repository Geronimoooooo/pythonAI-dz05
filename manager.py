import sys
import os
import shutil

import menu

while True:
    menu.show_menu()

    i = 0
    items = os.listdir()
    current_dir = os.getcwd()

    choice = input('Выберите пункт меню')
    if choice == '1':
        if not os.path.exist(f'new{i}'):
            os.mkdir(f'new{i}')
            i += 1
        pass
    elif choice == '2':
        os.rmdir(f'new{i}')
        pass
    elif choice == '3':
        file_to_copy = input('Введите название папки или файла: ')
        copied_file = input('Введите куда копировать: ')
        if not os.path.exist(file_to_copy):
            print('Такого файла или папки нет')
        else:
            shutil.copy(file_to_copy, copied_file)
        pass
    elif choice == '4':
        print(os.listdir())
        pass
    elif choice == '5':
        for item in items:
            if os.path.isfile(item):
                print('Вот только файлы: ', item)
        pass
    elif choice == '6':
        for item in items:
            if os.path.isdir(item):
                print('Вот только папки: ', item)
        pass
    elif choice == '7':
        print(sys.platform)
        pass
    elif choice == '8':
        user = os.environ.get('USERNAME') or os.environ.get('USER')
        print('Создатель программы:', user)
        pass
    elif choice == '9':
        menu.victorina()
        pass
    elif choice == '10':
        menu.my_bank_account()
        pass
    elif choice == '11':
        old_dir = current_dir
        new_dir = input('Введите новую директорию: ')
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
        else:
            print('Такой директории не существует')
        pass
    elif choice == '12':
        os.chdir(old_dir)
        pass
    elif choice == '13':
        menu.save_directory_in_file()
        pass
    elif choice == '0':
        break
    else:
        print('Неверный пункт меню')