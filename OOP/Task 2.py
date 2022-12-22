# Создайте симулятор из реальной жизни. Это может быть бронирование номера в гостинице, посещение казино, поход в бар.
# Создайте 3-4 объекта, которые могут описать ситуацию. Объекты должны содержать атрибуты и методы для моделирования
# некоторых случаев использования. Законченная программа должна выводить состояния объектов,
# их действия (методы) и взаимодействие объектов.

from random import randint
import time


class Person:

    def __init__(self, name, surname, sex, age, personal_account=2000, booked_rooms=0, alcohol_consumed=0):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.personal_account = personal_account
        self.booked_rooms = booked_rooms
        self.alcohol_consumed = alcohol_consumed
        self.vacation = None

    def take_vacation(self, days, vacation_type):
        self.vacation = Vacation(days, vacation_type)
        success = True
        return success

    def __repr__(self):
        return self.name


class Vacation:

    def __init__(self, days, vacation_type):
        self.days = days
        self.vacation_type = vacation_type

    def __repr__(self):
        return f'{self.days} days - {self.vacation_type}'


class Hotel:

    def __init__(self, name, room_stock=75, room_price=100):
        self.name = name
        self.room_stock = room_stock
        self.room_price = room_price

    def book_room(self, days, person):
        success = False

        if self.room_stock and person.personal_account >= self.room_price:
            need_money = self.room_price * days
            if person.personal_account >= need_money:
                self.room_stock -= 1
                person.booked_rooms += 1
                person.personal_account -= need_money
                print('Номер забронирован')
                success = True
        else:
            print('Свободных номеров нет')

        return success

    def __repr__(self):
        return self.name


class Bar:

    def __init__(self, name, bottles_of_alcohol=500, bottle_price=10):
        self.name = name
        self.bottles_of_alcohol = bottles_of_alcohol
        self.bottle_price = bottle_price

    def drink_alcohol(self, person):
        success = False

        if self.bottles_of_alcohol and not person.alcohol_consumed and person.personal_account >= self.bottle_price:
            self.bottles_of_alcohol -= 1
            person.alcohol_consumed += 1
            person.personal_account -= self.bottle_price
            print('Посетитель выпил бутылку алкоголя')
            success = True
        else:
            person.alcohol_consumed = 0
            print('Посетитель перебрал и сейчас в отключке. Бармен больше не наливает')
            time.sleep(1)
            print('Посетитель проспался и может дальше пить')

        return success

    def __repr__(self):
        return self.name


class Casino:

    def __init__(self, name, casino_balance=1000000, minimal_bet=10):
        self.name = name
        self.casino_balance = casino_balance
        self.minimal_bet = minimal_bet

    def make_bet(self, person, bet_amount):
        success = False

        if person.personal_account >= bet_amount >= self.minimal_bet \
                and self.minimal_bet <= bet_amount <= self.casino_balance:
            victory_numbers = [3, 7, 9]
            if randint(1, 10) in victory_numbers:
                person.personal_account += bet_amount
                self.casino_balance -= bet_amount
                print(f'Посетитель выиграл {bet_amount} долларов в казино!')
                success = True
            else:
                person.personal_account -= bet_amount
                self.casino_balance += bet_amount
                print(f'Посетитель проиграл {bet_amount} долларов в казино')
        else:
            print('У посетителя нет денег на ставку, либо посетитель сделал слишком низкую ставку')

        return success

    def __repr__(self):
        return self.name


ivan = Person('Ivan', 'Kozlov', 'm', 30)
ivan.take_vacation(20, 'paid')
print(ivan.vacation)

hotel_california = Hotel('California')
hotel_california.book_room(5, ivan)

bar_avos = Bar('Avos')
bar_avos.drink_alcohol(ivan)
bar_avos.drink_alcohol(ivan)

casino_grand = Casino('Grand')
casino_grand.make_bet(ivan, 3000)
casino_grand.make_bet(ivan, 1000)
