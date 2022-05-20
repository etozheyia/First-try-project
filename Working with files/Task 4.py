# Реализовать программу с базой учащихся группы (данные хранятся в json-файле). Записи по учащемуся:
# имя, фамилия, пол, возраст. Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.

import json

with open('task_4.json', encoding="utf8") as file:
    data = json.load(file)

ordinal_number = 0
for student in data['group']:
    ordinal_number += 1
    print(ordinal_number, student['first_name'], student['last_name'], student['gender'], student['age'])
