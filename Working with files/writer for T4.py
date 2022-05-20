import json

filename = 'task_4.json'

students = [{
    'first_name': 'Максим',
    'last_name': 'Андрейчиков',
    'gender': 'мужской',
    'age': 17
}, {
    'first_name': 'Ксения',
    'last_name': 'Гамезо',
    'gender': 'женский',
    'age': 17
}, {
    'first_name': 'Валерия',
    'last_name': 'Дмитрук',
    'gender': 'женский',
    'age': 16
}, {
    'first_name': 'Вячеслав',
    'last_name': 'Зубович',
    'gender': 'мужской',
    'age': 16
}, {
    'first_name': 'Вероника',
    'last_name': 'Карасик',
    'gender': 'женский',
    'age': 16
}, {
    'first_name': 'Светлана',
    'last_name': 'Карата',
    'gender': 'женский',
    'age': 17
}, {
    'first_name': 'Никита',
    'last_name': 'Кунцевич',
    'gender': 'мужской',
    'age': 17
}, {
    'first_name': 'Павел',
    'last_name': 'Михалёв',
    'gender': 'мужской',
    'age': 16
}, {
    'first_name': 'Дмитрий',
    'last_name': 'Неделько',
    'gender': 'мужской',
    'age': 16
}, {
    'first_name': 'Алина',
    'last_name': 'Пашкевич',
    'gender': 'женский',
    'age': 17
}, {
    'first_name': 'Анна',
    'last_name': 'Родионова',
    'gender': 'женский',
    'age': 16
}, {
    'first_name': 'Владислав',
    'last_name': 'Сакович',
    'gender': 'мужской',
    'age': 17
}, {
    'first_name': 'Анастасия',
    'last_name': 'Смоляк',
    'gender': 'женский',
    'age': 17
}, {
    'first_name': 'Кирилл',
    'last_name': 'Угольник',
    'gender': 'мужской',
    'age': 16
}, {
    'first_name': 'Яна',
    'last_name': 'Чернявская',
    'gender': 'женский',
    'age': 16
}]

to_json = {'group': students}
with open(filename, 'w') as file:
    json.dump(to_json, file, indent=3)
