# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней
# символов и слов.

filename = 'task_2.txt'
line_counter, words, symbol_counter = 0, 0, 0
with open(filename, 'r') as text:
    for line in text:
        line_counter += 1
        words = line.count(' ') + 1
        symbol_counter = len(line)
        print(f'Строка №{line_counter}, Количество слов:{words}, Количество символов:{symbol_counter}')
    print(f'Количество строк:{line_counter}')
