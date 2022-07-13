# Создайте симулятор из реальной жизни. Это может быть бронирование номера в гостинице, посещение казино, поход в бар.
# Создайте 3-4 объекта, которые могут описать ситуацию. Объекты должны содержать атрибуты и методы для моделирования
# некоторых случаев использования. Законченная программа должна выводить состояния объектов,
# их действия (методы) и взаимодействие объектов.

# Я не стал делать атрибуты приватными и писать под них сеттеры и валидаторы, т.к. это дополнительные объёмы строк кода
# для каждого класса. Их тут и так не мало получилось. Ограничился атрибутами, выставленными по умолчанию. Но я понимаю,
# что можно было так сделать (в идеале, конечно, так и нужно сделать).

from random import randint


class Vacation:

    name = 'Ivan'
    age = 25
    occupation = 'tourist'

    def __init__(self, personal_account=2000, booked_rooms=0, alcohol_consumed=0):
        self.personal_account = personal_account
        self.booked_rooms = booked_rooms
        self.alcohol_consumed = alcohol_consumed

    def get_values(self):
        return {'name': self.name, 'age': self.age, 'occupation': self.occupation,
                'personal account': self.personal_account, 'booked rooms': self.booked_rooms,
                'alcohol consumed': self.alcohol_consumed}


class Hotel:

    name = 'Anna'
    age = 29
    occupation = 'receptionist'
    workplace = 'reception'

    def __init__(self, room_stock=75):
        self.room_stock = room_stock

    def reservation(self, other):
        if isinstance(other, Vacation):
            if other.booked_rooms == 0:
                self.room_stock -= 1
                other.booked_rooms += 1
                other.personal_account = other.personal_account - ((other.personal_account // 100) * 15)
                print('Номер забронирован')
                return self.room_stock, other.booked_rooms, other.personal_account
            else:
                print('Клиент уже забронировал номер')
                return other.booked_rooms
        raise TypeError('Параметр должен иметь тип Vacation')

    def get_values(self):
        return {'name': self.name, 'age': self.age, 'occupation': self.occupation,
                'workplace': self.workplace, 'room stock': self.room_stock, 'action': 'reservation'}


class Bar:

    name = 'Boris'
    age = 33
    occupation = 'bartender'
    workplace = 'bar counter'

    def __init__(self, bottles_of_alcohol=500):
        self.bottles_of_alcohol = bottles_of_alcohol

    def alcohol_bottling(self, other):
        if isinstance(other, Vacation):
            if other.alcohol_consumed <= 1:
                self.bottles_of_alcohol -= 1
                other.personal_account = other.personal_account - ((other.personal_account // 100) * 0.15)
                other.alcohol_consumed += 1
                print('Посетитель выпил бутылку алкоголя')
                return self.bottles_of_alcohol, other.alcohol_consumed, other.personal_account
            else:
                print('Посетитель перебрал и сейчас в отключке. Бармен больше не наливает')
                other.alcohol_consumed = 0
                print('Посетитель проспался и может дальше пить')
                return other.alcohol_consumed
        raise TypeError('Параметр должен иметь тип Vacation')

    def get_values(self):
        return {'name': self.name, 'age': self.age, 'occupation': self.occupation,
                'workplace': self.workplace, 'bottles of alcohol': self.bottles_of_alcohol,
                'action': 'alcohol bottling'}


class Casino:

    name = 'Kate'
    age = 24
    occupation = 'croupier'
    workplace = 'gambling table'

    def __init__(self, casino_balance=1000000, minimal_bet=10):
        self.casino_balance = casino_balance
        self.minimal_bet = minimal_bet

    def gambling(self, other, game_bet):
        if isinstance(other, Vacation):
            if other.personal_account >= self.minimal_bet and game_bet >= self.minimal_bet:
                grn = randint(1, 10)
                if grn == 3 or grn == 7 or grn == 9:
                    other.personal_account += game_bet
                    self.casino_balance -= game_bet
                    print(f'Посетитель выиграл {game_bet} долларов в казино!')
                    return self.casino_balance, other.personal_account
                else:
                    other.personal_account -= game_bet
                    self.casino_balance += game_bet
                    print(f'Посетитель проиграл {game_bet} долларов в казино')
                    return self.casino_balance, other.personal_account
            else:
                print('У посетителя нет денег на ставку, либо посетитель сделал слишком низкую ставку')
                return other.personal_account, game_bet, self.minimal_bet
        raise TypeError('Параметр должен иметь тип Vacation')

    def get_values(self):
        return {'name': self.name, 'age': self.age, 'occupation': self.occupation,
                'workplace': self.workplace, 'casino balance': self.casino_balance, 'minimal bet': self.minimal_bet,
                'action': 'gambling'}


Ivan = Vacation()
Boris = Bar()
Anna = Hotel()
Kate = Casino()
print(Anna.reservation(Ivan))
print(Anna.reservation(Ivan))
print(Kate.gambling(Ivan, 9))
print(Kate.gambling(Ivan, 50))
print(Boris.alcohol_bottling(Ivan))
print(Boris.alcohol_bottling(Ivan))
print(Boris.alcohol_bottling(Ivan))
print(Boris.alcohol_bottling(Ivan))
print(Ivan.get_values())
print(Anna.get_values())
print(Boris.get_values())
print(Kate.get_values())
