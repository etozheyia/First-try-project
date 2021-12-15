# Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца,
# в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот,
# у которого меньше номер строки. А если номера строк равны, то тот, у которого меньше номер столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.

d = input().split()
n, m = int(d[0]), int(d[1])
a = [[int(e) for e in input().split()] for r in range(n)]
row_with_max = max(a)
max_elem = max(row_with_max)
min_s, min_c = 0, 0

for s in range(n):
    for c in range(m):
        if a[s][c] == max_elem:
            if min_s < n and min_c < m:
                min_s, min_c = s, c
                print(min_s, min_c)
                min_s, min_c = n + 1, m + 1
