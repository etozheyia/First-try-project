# Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего
# элемента последовательности.

n = int(input())
maximum = 0
while n != 0:
    if n > maximum:
        maximum = n
    n = int(input())
print(maximum)
