# Дан список кортежей grades = [(‘Ann’, 9), (‘John’, 7), (‘Smith’, 5), (‘George’, 6) ].
# Вывести информацию об оценках по возрастанию в виде:
# ‘Hello Ann! Your grade is 9’

grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]
grades.sort(key=lambda x: x[1])
grades = [list(i) for i in grades]
journal = []

for row in grades:
    for elem in row:
        journal.append(str(elem))

for i in range(1, len(journal), 2):
    print('Hello ' + journal[i - 1] + '! ' + 'Your grade is ' + journal[i])


# альтернативное решение
grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]

for name, mark in sorted(grades, key=lambda x: x[1]):
    print(f'Hello {name}! Your grade is {mark}')
