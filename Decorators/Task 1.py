# Даны строка и словарь. Необходимо, используя декоратор, записать эти 2 объекта в разные файлы:
# словарь записать в json-файл, а строку - в текстовый.

def data_writer(func):
    import json

    def wrapper(string, dictionary):
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
