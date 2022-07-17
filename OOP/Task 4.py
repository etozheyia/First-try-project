# Реализовать программу с базой учащихся группы (данные хранятся в файле). Записи по учащемуся должны быть представлены
# отдельным классом с полями: имя, фамилия, пол, возраст. Программа должна предусматривать поиск по одному или
# нескольким полям базы. Результат выводить в удобочитаемом виде с порядковым номером записи. Скрипт программы
# должен принимать параметр, который определяет формат хранения и реализации БД: в текстовом файле с
# определенной структурой; в файле json.
#
# Json можно использовать такой:
# [{"Sex": "male", "Surname": "Olegov", "Age": "20", "Name": "Oleg"},
#  {"Sex": "female", "Surname": "Katina", "Age": "30", "Name": "Katya"},
#  {"Sex": "male", "Surname": "Sashov", "Age": "22", "Name": "Sasha"},
#  {"Sex": "male", "Surname": "Dmitriev", "Age": "33", "Name": "Dmitryi"}]
#
# А текстовый файл такой:
# Oleg Olegov  male  20
# Katya Katina  female  30
# Sasha Sashov  male  22
# Dmitryi Dmitriev  male  33

import json


class Person:

    def __init__(self, name, surname, sex, age):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age


class Oleg(Person):
    pass


class Sasha(Person):
    pass


class Dmitryi(Person):
    pass


class Katya(Person):
    pass


print('Введите одну из команд: '
      '"set_json_data" - определить формат базы данных как json; '
      '"set_txt_data" - определить формат базы данных как txt')

command = input('Какой формат вы хотите установить?:')

try:
    if command == 'set_json_data':

        students_json = [{"Sex": "male", "Surname": "Olegov", "Age": "20", "Name": "Oleg"},
                         {"Sex": "female", "Surname": "Katina", "Age": "30", "Name": "Katya"},
                         {"Sex": "male", "Surname": "Sashov", "Age": "22", "Name": "Sasha"},
                         {"Sex": "male", "Surname": "Dmitriev", "Age": "33", "Name": "Dmitryi"}]

        to_json = {'group': students_json}
        with open('oop_task_4.json', 'w') as file_json:
            json.dump(to_json, file_json, indent=3)

        with open('oop_task_4.json', 'r', encoding="utf8") as file_json:
            data = json.load(file_json)

            ordinal_number = 0
            for student in data['group']:
                if student['Name'] == 'Oleg':
                    student_Oleg = Oleg(student['Name'], student['Surname'], student['Sex'], student['Age'])
                    ordinal_number += 1
                    print(ordinal_number, student_Oleg.get_name(), student_Oleg.get_surname(),
                          student_Oleg.get_sex(), student_Oleg.get_age())
                elif student['Name'] == 'Sasha':
                    student_Sasha = Sasha(student['Name'], student['Surname'], student['Sex'], student['Age'])
                    ordinal_number += 1
                    print(ordinal_number, student_Sasha.get_name(), student_Sasha.get_surname(),
                          student_Sasha.get_sex(), student_Sasha.get_age())
                elif student['Name'] == 'Dmitryi':
                    student_Dima = Dmitryi(student['Name'], student['Surname'], student['Sex'], student['Age'])
                    ordinal_number += 1
                    print(ordinal_number, student_Dima.get_name(), student_Dima.get_surname(),
                          student_Dima.get_sex(), student_Dima.get_age())
                else:
                    student_Kate = Katya(student['Name'], student['Surname'], student['Sex'], student['Age'])
                    ordinal_number += 1
                    print(ordinal_number, student_Kate.get_name(), student_Kate.get_surname(),
                          student_Kate.get_sex(), student_Kate.get_age())

    elif command == 'set_txt_data':

        students_txt = ['Oleg Olegov  male  20',
                        'Katya Katina  female  30',
                        'Sasha Sashov  male  22',
                        'Dmitryi Dmitriev  male  33']

        with open('oop_task_4.txt', 'a') as file_txt:
            for line in students_txt:
                file_txt.write(line + ' \n')

        with open('oop_task_4.txt', 'r') as file_txt:
            ordinal_number = 0
            name_index, surname_index, sex_index, age_index = 0, 1, 2, 3
            for row in file_txt:
                student_row = row.split(' ')
                student_row.remove('')
                student_row.remove('')
                if student_row[name_index] == 'Oleg':
                    student_Oleg = Oleg(student_row[name_index], student_row[surname_index],
                                        student_row[sex_index], student_row[age_index])
                    ordinal_number += 1
                    print(ordinal_number, student_Oleg.get_name(), student_Oleg.get_surname(),
                          student_Oleg.get_sex(), student_Oleg.get_age())
                elif student_row[name_index] == 'Sasha':
                    student_Sasha = Sasha(student_row[name_index], student_row[surname_index],
                                          student_row[sex_index], student_row[age_index])
                    ordinal_number += 1
                    print(ordinal_number, student_Sasha.get_name(), student_Sasha.get_surname(),
                          student_Sasha.get_sex(), student_Sasha.get_age())
                elif student_row[name_index] == 'Dmitryi':
                    student_Dima = Dmitryi(student_row[name_index], student_row[surname_index],
                                           student_row[sex_index], student_row[age_index])
                    ordinal_number += 1
                    print(ordinal_number, student_Dima.get_name(), student_Dima.get_surname(),
                          student_Dima.get_sex(), student_Dima.get_age())
                else:
                    student_Kate = Katya(student_row[name_index], student_row[surname_index],
                                         student_row[sex_index], student_row[age_index])
                    ordinal_number += 1
                    print(ordinal_number, student_Kate.get_name(), student_Kate.get_surname(),
                          student_Kate.get_sex(), student_Kate.get_age())

        with open('oop_task_4.txt', 'w') as file_txt:
            file_txt.write('')

    else:
        print('Ошибка имени')
        raise NameError

except NameError:
    print('Введена недопустимая команда')

print(student_Oleg.get_name(), student_Oleg.get_age())
print(student_Kate.get_surname(), student_Kate.get_sex())
print(student_Sasha.get_sex(), student_Sasha.get_surname())
print(student_Dima.get_age(), student_Dima.get_name())
