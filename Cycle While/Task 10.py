# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих
# элементов этой последовательности равны друг другу.

number = int(input())
count = 1
max_count = 0
while number != 0:
    next_number = int(input())
    number, next_number = next_number, number
    if next_number == number:
        count += 1
    if count > max_count:
        max_count = count
    if number != next_number:
        count = 1
print(max_count)
