# Последовательность состоит из натуральных чисел и завершается числом 0. Определите индекс наибольшего элемента
# последовательности. Если наибольших элементов несколько, выведите индекс первого из них.
# Нумерация элементов начинается с нуля.

n = int(input())
i, maximum, i_max = 0, 0, 0
while n != 0:
    if n > maximum:
        maximum = n
        i_max = i
    n = int(input())
    i += 1
print(i_max)
