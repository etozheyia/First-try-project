# Задание по модулям.
# Функции generate_numbers, count_characters, fizzbuzz, is_palindrome сделать фейковыми, то есть
# просто написать внутри случайный return что-то. return [1, 2, 3] или return True.

# 1. Напишите два модуля pytasks.py и runner.py. Модуль pytasks содержит определения функций.
# Отдельный модуль runner содержит функцию runner(). Модуль runner может быть импортирован или запущен из командной
# строки как сценарий.
# ● generate_numbers()
# ● count_characters()
# ● fizzbuzz() - возвращает список со значениями
# ● is_palindrome() - возвращает True или False.
# Функция runner() может быть вызвана как:
# runner() - все функции будут вызваны со значениями по умолчанию, а результат выведен на экран
# runner('generate_numbers') - вывод результата только для функции generate_numbers()
# runner('generate_numbers', 'happy_numbers') - вывод результатов для generate_numbers() и happy_numbers().
# Можно указать любую комбинацию функций.

def generate_numbers():
    return 5


def count_characters():
    return 10 + 10


def fizzbuzz():
    return [1, 2, 3]


def is_palindrome():
    return True
