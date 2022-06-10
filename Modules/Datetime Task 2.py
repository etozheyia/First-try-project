# Пользователь вводит две даты (формат даты, вводимой пользователем, выберите любой – через точку, запятую
# или тире – на ваше усмотрение). Определить количество прошедших дней между ними.

from datetime import datetime

first_date = input('Введите первую дату (формат "dd-mm-yyyy"):')
second_date = input('Введите вторую дату (формат "dd-mm-yyyy"):')
dt_first_date = datetime.strptime(first_date, '%d-%m-%Y')
dt_second_date = datetime.strptime(second_date, '%d-%m-%Y')
difference = abs(dt_first_date - dt_second_date)
print(f'Между датами прошло/пройдёт {difference.days} дней')
