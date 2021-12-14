# Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой
# последовательности больше предыдущего элемента.

n, previous, larger_number = 0.5, 0, -1
while n != 0:
    n = int(input())
    if n > previous:
        larger_number += 1
    previous = n
print(larger_number)
