# Задача 6.
# Реализовать программу, позволяющую осуществлять управление файлами: копирование, создание, удаление, переименование.
# Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.

import os


def copy(filename):
    with open(filename, encoding="utf8") as file:
        data = file.read()
    with open('file_copy.txt', 'w') as new_file:
        new_file.write(data)


print('Что вы хотите сделать с файлом/директорией? '
      '"copy" - копировать файл, '
      '"create" - создать новый файл, '
      '"remove" - удалить файл, '
      '"rename" - переименовать файл, '
      '"check" - вывести текущую директорию, '
      '"change" - изменить директорию')
action = input()

while action:
    if action == 'copy':
        print('Укажите путь к файлу для копирования')
        path_to_copy = input()
        copy(path_to_copy)
    elif action == 'create':
        print('Укажите имя нового файла (имя должно содержать расширение ".txt")')
        file_name = input()
        with open(file_name, 'w+', encoding="utf8") as created_file:
            print('Введите данные для нового файла')
            text = input()
            created_file.write(text)
    elif action == 'remove':
        print('Укажите путь к файлу, который следует удалить')
        path_to_delete = input()
        os.remove(path_to_delete)
    elif action == 'rename':
        print('Укажите путь к файлу, который следует переименовать')
        path_to_rename = input()
        print('Введите новое имя файла')
        new_name = input()
        os.rename(path_to_rename, new_name)
    elif action == 'check':
        print('Текущая директория:', os.getcwd())
    elif action == 'change':
        print('Укажите путь к новой директории')
        path_to_folder = input()
        os.chdir(path_to_folder)
    action = input()
