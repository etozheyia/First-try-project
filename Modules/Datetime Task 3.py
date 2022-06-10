# Определить количество дней между датой, введенной пользователем, и сегодняшним днем.

from datetime import datetime

user_date = input('Введите дату (формат "dd-mm-yyyy"):')
dt_user_date = datetime.strptime(user_date, '%d-%m-%Y')
today_date = datetime.now()
difference = abs(today_date - dt_user_date)
print(f'Между вашей датой и сегодняшним днём прошло/пройдёт {difference.days} дней')
