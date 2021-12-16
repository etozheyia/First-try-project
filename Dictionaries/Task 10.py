# Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись
# вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название товара
# (строка без пробелов), количество — количество приобретенных единиц товара.
#
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого
# вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить
# в лексикографическом порядке.

from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)

for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])
