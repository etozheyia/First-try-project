# Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
# Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести
# количество членов последовательности (не считая завершающего числа 0).
# Числа, следующие за числом 0, считывать не нужно.

n = int(input())
amount = 0
while n != 0:
    amount += 1
    n = int(input())
print(amount)
