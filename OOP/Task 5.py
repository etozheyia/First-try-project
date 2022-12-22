# Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта.
# При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции.
# Если производить вычитание у лифта, который еще не совершал поднятий, должна быть выведена ошибка неправильной
# операции. Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
# Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
# При строчных операциях необходимо вывести детальную информацию по лифту: наименование, количество поднятий и процент
# от общего количества поднятий всех лифтов.
# Для вычисления процента от общего количества - число делится на общее количество и умножается на 100

class Elevator:

    def __init__(self, name, lift_counter=0, current_floor=1, percent_of_total_lifts=0):
        self.name = name
        self.lift_counter = lift_counter
        self.current_floor = current_floor
        self.percent_of_total_lifts = percent_of_total_lifts

    def lift_up(self, floor_number):
        self.lift_counter += 1
        self.current_floor += floor_number
        return self.current_floor

    def lift_down(self, floor_number):
        if self.lift_counter and self.current_floor > floor_number:
            self.lift_counter += 1
            self.current_floor -= floor_number
            return self.current_floor
        else:
            print('Лифт ещё не совершал поднятий или количество этажей равно либо превышает текущий этаж')
            raise NotImplementedError

    def __gt__(self, other):
        return self.lift_counter > other.lift_counter

    def get_elevators_total_lifts(self, elevators: list) -> int:
        total_lifts = sum([self.lift_counter for self.name in elevators])
        return total_lifts

    def get_percent_of_total_lifts(self, total_lifts):
        self.percent_of_total_lifts = (self.lift_counter / total_lifts) * 100
        return self.percent_of_total_lifts

    def __repr__(self):
        return self.name, self.lift_counter, self.percent_of_total_lifts
