# Реализовать модуль, содержащий следующие функции декораторы:
# 1. Декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
# 2. Декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
# 3. Декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
# 4. Декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        end = time.time()
        print(f'Время работы функции: {end - start} секунд')
        return rv
    return wrapper


def data_writer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        end = time.time()
        func_time = f'Время работы функции: {end - start} секунд'
        func_name = func.__name__
        with open('function_info.txt', 'w') as file:
            file.write(f'Имя фукции: {func_name}')
        with open('function_info.txt', 'a') as file:
            file.write('\n' + func_time)
            if args:
                file.write('\nПозиционные параметры функции: ')
                for item in args:
                    file.write(str(item) + ' ')
            if kwargs:
                file.write(f'\nИменованные параметры функции: ')
                for value in kwargs.values():
                    file.write(str(value) + ' ')
        return rv
    return wrapper


def type_checker(func):
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        if args:
            print('Типы позиционных параметров:')
            for item in args:
                print(type(item))
        if kwargs:
            print('Типы именованных параметров:')
            for value in kwargs.values():
                print(type(value))
        if not args and not kwargs:
            print('Функция не имеет параметров')
        return rv
    return wrapper


def cache(func):
    memory = {}

    def wrapper(*args, **kwargs):
        nonlocal memory
        if not memory.get(args):
            remember = func(*args, **kwargs)
            memory[args] = remember
            return remember
        else:
            return memory[args]
    return wrapper
