# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
#
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
#
# Решение оформите в виде функции swap_columns(a, i, j).

def swap_columns(a, i, j):
    index_i = a.index(a[i])
    index_j = a.index(a[j])
    elem_i, elem_j = 0, 0

    if index_i != index_j:
        for i in range(len(a)):
            if i == index_i:
                elem_i = a[i]
            elif i == index_j:
                elem_j = a[i]

        for e in range(len(a)):
            if a[e] == elem_i:
                a[e] = elem_j
            elif a[e] == elem_j:
                a[e] = elem_i
        return a
    else:
        return a


n, m = [int(i) for i in input().split()]
a = [[int(e) for e in input().split()] for row in range(n)]
i, j = [int(i) for i in input().split()]

for row in a:
    swap_columns(row, i, j)
    print(' '.join([str(e) for e in row]))
