# Напишите функцию, которая будет принимать дату в строковом формате и возвращать дату на неделю позже.

from datetime import datetime, timedelta


def week_later(date, date_format):
    assert type(date) == str, 'Дата должна быть в строковом формате'
    incoming_date = datetime.strptime(date, date_format)
    seven_days = timedelta(7)
    returned_date = incoming_date + seven_days
    return returned_date
