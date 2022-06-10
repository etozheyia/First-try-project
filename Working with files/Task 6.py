# Реализовать программу, позволяющую осуществлять управление файлами: копирование, создание, удаление, переименование.
# Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.

import os


def copy(filename):
    assert len(filename) != 0, 'Путь к файлу не был указан'
    assert filename[-4:] == '.txt', 'Копируемый файл не имеет расширения ".txt"'
    try:
        with open(filename) as file:
            data = file.read()
    except FileNotFoundError:
        print('Был указан некорректный путь')
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
        assert len(file_name) != 0, 'Вы не указали имя нового файла'
        assert file_name[-4:] == '.txt', 'Файл не имеет расширения ".txt"'
        with open(file_name, 'w+') as created_file:
            print('Введите данные для нового файла')
            text = input()
            created_file.write(text)
    elif action == 'remove':
        print('Укажите путь к файлу, который следует удалить')
        path_to_delete = input()
        assert len(path_to_delete) != 0, 'Путь к файлу не был указан'
        try:
            os.remove(path_to_delete)
        except FileNotFoundError:
            print('Был указан некорректный путь')
    elif action == 'rename':
        print('Укажите путь к файлу, который следует переименовать')
        path_to_rename = input()
        assert len(path_to_rename) != 0, 'Путь к файлу не был указан'
        print('Введите новое имя файла')
        new_name = input()
        assert len(new_name) != 0, 'Вы не указали новое имя файла'
        try:
            os.rename(path_to_rename, new_name)
        except FileNotFoundError:
            print('Был указан некорректный путь')
    elif action == 'check':
        print('Текущая директория:', os.getcwd())
    elif action == 'change':
        print('Укажите путь к новой директории')
        path_to_folder = input()
        assert len(path_to_folder) != 0, 'Путь к новой директории не был указан'
        try:
            os.chdir(path_to_folder)
        except FileNotFoundError:
            print('Был указан некорректный путь')
    else:
        print('Вы ввели некорректную команду')
    action = input('Что вы хотите сделать с файлом/директорией? :')
