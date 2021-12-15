# Реализовать функцию get_ranges. Которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию. И которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"

def get_ranges(a):
    ranges = []
    new_list = ''

    for i in range(1, len(a)):
        if a[i - 1] + 1 == a[i]:
            ranges.append(a[i - 1])
        elif a[i - 1] not in ranges:
            ranges.append(a[i - 1])
            if len(ranges) > 1:
                min_el, max_el = min(ranges), max(ranges)
                new_list += str(min_el) + '-' + str(max_el) + ' '
                ranges = []
            elif len(ranges) == 1:
                new_list += str(ranges[0]) + ' '
                ranges = []
    if len(ranges) != 0:
        new_list += str(ranges[0]) + '-'
    new_list += str(a[-1])
    new_list = new_list.replace(' ', ',')
    return new_list


roster = [int(i) for i in input().split()]  # на ввод подается строка из целых чисел через пробел
print(get_ranges(roster))                   # при считывании, она будет преобразована в список
