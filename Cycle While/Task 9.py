# Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой
# последовательности равны ее наибольшему элементу.

n = int(input())
maximum, count_max = 0, 0
while n != 0:
    if n > maximum:
        maximum = n
        count_max = 1
    elif maximum == n:
        count_max += 1
    n = int(input())
print(count_max)
