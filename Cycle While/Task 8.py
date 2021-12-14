# Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по
# величине элемента в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.

n = int(input())
maximum, prev_maximum = 0, 0
while n != 0:
    if n > maximum:
        prev_maximum = maximum
        maximum = n
    elif maximum > n > prev_maximum:
        prev_maximum = n
    n = int(input())
print(prev_maximum)
