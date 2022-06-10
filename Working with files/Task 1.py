# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
# пустая строка.

filename = 'task_1.txt'
text = []
print('Введите строку данных')
line = input()
while line:
    text.append(line + '\n')
    print('Введите новую строку данных')
    line = input()
text.append('')

with open(filename, 'a') as file:
    for line in text:
        file.write(line)
