# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

states = dict()
for line in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        states[city] = country

for i in range(int(input())):
    city = input()
    print(states[city])


# альтернативное решение (с поиском ключа по значению)
countries = {}

for _ in range(int(input())):
    country, *cities = input().split()
    countries[country] = cities

for _ in range(int(input())):
    city = input()
    for country in countries.keys():
        if city in countries[country]:
            print(country)
