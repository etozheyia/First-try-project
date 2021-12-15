# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.

n, m = [int(i) for i in input().split()]
a = [['.'] * m for i in range(n)]

for s in range(n):
    if (s + 1) % 2 != 0:
        for c in range(1, m, 2):
            a[s][c] = '*'
    else:
        for c in range(0, m, 2):
            a[s][c] = '*'

for row in a:
    print(' '.join(row))
