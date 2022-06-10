# Даны строка и словарь. Необходимо, используя декоратор, записать эти 2 объекта в разные файлы:
# словарь записать в json-файл, а строку - в текстовый.

import json


def data_writer(func):
    def wrapper(string, dictionary):
        assert type(string) == str, 'Переданный аргумент не является строкой'
        assert type(dictionary) == dict, 'Переданный аргумент не является словарём'
        func(string, dictionary)
        with open('string_file.txt', 'w') as file:
            file.write(string)
        with open('dict_file.json', 'w') as file:
            json.dump(dictionary, file, indent=2)
    return wrapper


@data_writer
def data_provider(st, di):
    return st, di


profile = {'name': 'Anna',
           'age': 24,
           'height': 179,
           'weight': 70
           }
data_provider('This string has to be written', profile)
